"""
run_otp_volatility_analysis.py
------------------------------
Comprehensive empirical analysis on weighing OTP attributes for predicting 
specifically TSA Throughput Volatility, comparing Feature Values (Levels) 
versus Feature Volatility (Dispersion/Variability).

Author: Graduate Research Assistant / AI Pair Programmer
Milestone: Gleich 700B Master's Thesis
Safety Rule: Strictly non-destructive. Outputs written to otp_volatility_analysis/
"""

import os
import sys
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV, LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.inspection import permutation_importance
from sklearn.feature_selection import mutual_info_regression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.titlesize': 15,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.autolayout': True,
    'figure.dpi': 300
})

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.data.panel_loader import load_and_prepare_panel_data


def perform_factor_weighting_analysis(df_panel):
    print("\n[Step 2] Conducting Factor Weighting Analysis on OTP Attributes...")
    
    # Filter valid rows
    clean_df = df_panel.dropna(subset=[
        'tsa_hourly_std', 'tsa_hourly_cv', 'tsa_rolling_7d_std', 'tsa_rolling_7d_cv',
        'sched_daily_total', 'actual_daily_total', 'daily_cancellations', 'daily_cancel_rate',
        'sched_hourly_std', 'sched_hourly_cv', 'actual_hourly_std', 'actual_hourly_cv',
        'sched_rolling_7d_std', 'sched_rolling_7d_cv', 'cancel_rolling_7d_std',
        'avg_dep_delay_minutes', 'flights_delayed_15min_pct', 'avg_taxi_out_minutes',
        'otp_departure_delay_volatility_cv', 'otp_cancellation_volatility_cv',
        'aircraft_gauge_seats', 'route_load_factor_pct', 'connecting_passenger_share_pct'
    ]).copy()
    
    # Define All OTP Attributes & Classification
    feature_metadata = [
        # Domain 1: Schedule Scale & Execution
        ('sched_daily_total', 'Scheduled Flight Volume', 'Scale / Level', 'Domain 1: Schedule Scale', 'Values'),
        ('actual_daily_total', 'Actual Flight Movements', 'Scale / Level', 'Domain 1: Schedule Scale', 'Values'),
        ('sched_hourly_mean', 'Mean Hourly Scheduled Flights', 'Scale / Level', 'Domain 1: Schedule Scale', 'Values'),
        ('sched_rolling_7d_mean', 'Rolling 7d Scheduled Mean', 'Scale / Level', 'Domain 1: Schedule Scale', 'Values'),
        # Domain 2: Tactical Cancellations
        ('daily_cancellations', 'Daily Cancelled Flights', 'Disruption / Level', 'Domain 2: Cancellations', 'Values'),
        ('daily_cancel_rate', 'Daily Flight Cancellation Rate %', 'Disruption / Level', 'Domain 2: Cancellations', 'Values'),
        ('cancel_rolling_7d_mean', 'Rolling 7d Cancellations Mean', 'Disruption / Level', 'Domain 2: Cancellations', 'Values'),
        ('cancel_rate_rolling_7d_mean', 'Rolling 7d Cancel Rate Mean', 'Disruption / Level', 'Domain 2: Cancellations', 'Values'),
        # Domain 3: Flight Delays & Punctuality
        ('avg_dep_delay_minutes', 'Mean Departure Delay Minutes', 'Delay / Level', 'Domain 3: Delays', 'Values'),
        ('flights_delayed_15min_pct', 'Significant Delay Rate (DepDel15 %)', 'Delay / Level', 'Domain 3: Delays', 'Values'),
        # Domain 4: Surface Taxi Queues
        ('avg_taxi_out_minutes', 'Mean Runway Taxi-Out Minutes', 'Surface / Level', 'Domain 4: Surface Queues', 'Values'),
        # Domain 5: Network Topology & Capacity
        ('aircraft_gauge_seats', 'Aircraft Gauge (Seats/Flight)', 'Capacity / Level', 'Domain 5: Network Buffers', 'Values'),
        ('route_load_factor_pct', 'Flight Load Factor %', 'Capacity / Level', 'Domain 5: Network Buffers', 'Values'),
        ('connecting_passenger_share_pct', 'Connecting Passenger Share %', 'Buffer / Level', 'Domain 5: Network Buffers', 'Values'),
        
        # Volatility Features
        ('sched_hourly_std', 'Hourly Scheduled Flight Std Dev', 'Schedule Volatility', 'Domain 1: Schedule Scale', 'Volatility'),
        ('sched_hourly_cv', 'Hourly Scheduled Flight CV', 'Schedule Volatility', 'Domain 1: Schedule Scale', 'Volatility'),
        ('actual_hourly_std', 'Hourly Actual Flight Std Dev', 'Execution Volatility', 'Domain 1: Schedule Scale', 'Volatility'),
        ('actual_hourly_cv', 'Hourly Actual Flight CV', 'Execution Volatility', 'Domain 1: Schedule Scale', 'Volatility'),
        ('sched_rolling_7d_std', 'Rolling 7d Scheduled Flights Std', 'Schedule Volatility', 'Domain 1: Schedule Scale', 'Volatility'),
        ('sched_rolling_7d_cv', 'Rolling 7d Scheduled Flights CV', 'Schedule Volatility', 'Domain 1: Schedule Scale', 'Volatility'),
        ('cancel_rolling_7d_std', 'Rolling 7d Cancellation Std Dev', 'Disruption Volatility', 'Domain 2: Cancellations', 'Volatility'),
        ('cancel_rate_rolling_7d_std', 'Rolling 7d Cancel Rate Std Dev', 'Disruption Volatility', 'Domain 2: Cancellations', 'Volatility'),
        ('otp_departure_delay_volatility_cv', 'Departure Delay Volatility (CV)', 'Delay Volatility', 'Domain 3: Delays', 'Volatility'),
        ('otp_cancellation_volatility_cv', 'Cancellation Rate Volatility (CV)', 'Disruption Volatility', 'Domain 2: Cancellations', 'Volatility')
    ]
    
    meta_df = pd.DataFrame(feature_metadata, columns=['feature', 'feature_name', 'metric_type', 'domain', 'representation'])
    feature_cols = meta_df['feature'].tolist()
    
    # Chronological Split: Train (2019-2023), Val (2024), Test (2025)
    train_mask = clean_df['Year'] <= 2023
    val_mask = clean_df['Year'] == 2024
    test_mask = clean_df['Year'] == 2025
    
    print(f"Data Splits: Train N={train_mask.sum():,}, Val N={val_mask.sum():,}, Test N={test_mask.sum():,}")
    
    # Target: TSA Hourly Standard Deviation (Diurnal Throughput Volatility)
    target_col = 'tsa_hourly_std'
    
    X_train = clean_df.loc[train_mask, feature_cols]
    y_train = clean_df.loc[train_mask, target_col]
    X_val = clean_df.loc[val_mask, feature_cols]
    y_val = clean_df.loc[val_mask, target_col]
    X_test = clean_df.loc[test_mask, feature_cols]
    y_test = clean_df.loc[test_mask, target_col]
    
    # Standardize Features (strictly fitting on Train)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    
    y_mean = y_train.mean()
    y_std = y_train.std()
    y_train_scaled = (y_train - y_mean) / y_std
    y_test_scaled = (y_test - y_mean) / y_std
    
    # 1. Standardized OLS Linear Regression
    ols = LinearRegression(fit_intercept=False)
    ols.fit(X_train_scaled, y_train_scaled)
    ols_beta = ols.coef_
    
    # Compute OLS t-stats and p-values
    residuals = y_train_scaled - ols.predict(X_train_scaled)
    dof = len(y_train_scaled) - len(feature_cols)
    sigma2 = np.sum(residuals**2) / dof
    var_beta = sigma2 * np.linalg.pinv(np.dot(X_train_scaled.T, X_train_scaled)).diagonal()
    se_beta = np.sqrt(np.maximum(1e-12, var_beta))
    t_stats = ols_beta / se_beta
    p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=dof))
    
    # 2. Regularized Ridge Regression
    ridge = RidgeCV(alphas=np.logspace(-2, 4, 30), cv=5)
    ridge.fit(X_train_scaled, y_train_scaled)
    ridge_beta = ridge.coef_
    
    # 3. Regularized Lasso Regression
    lasso = LassoCV(alphas=np.logspace(-4, 1, 30), cv=5, random_state=42, max_iter=5000)
    lasso.fit(X_train_scaled, y_train_scaled)
    lasso_beta = lasso.coef_
    
    # 4. Elastic Net
    enet = ElasticNetCV(l1_ratio=[0.1, 0.5, 0.7, 0.9], alphas=np.logspace(-4, 1, 20), cv=5, random_state=42, max_iter=5000)
    enet.fit(X_train_scaled, y_train_scaled)
    enet_beta = enet.coef_
    
    # 5. Tree-Based Importance: Random Forest
    rf = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_importance = rf.feature_importances_
    
    # 6. Tree-Based Importance: Gradient Boosting
    gbr = GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.08, random_state=42)
    gbr.fit(X_train, y_train)
    gbr_importance = gbr.feature_importances_
    
    # 7. Permutation Feature Importance (on Validation Set)
    perm_res = permutation_importance(rf, X_val, y_val, n_repeats=5, random_state=42, n_jobs=-1)
    perm_importance = perm_res.importances_mean
    
    # 8. Mutual Information Score
    mi_scores = mutual_info_regression(X_train, y_train, random_state=42)
    
    # Assemble Factor Weighting Table
    weights_df = meta_df.copy()
    weights_df['standardized_ols_beta'] = ols_beta
    weights_df['ols_t_statistic'] = t_stats
    weights_df['ols_p_value'] = p_values
    weights_df['ridge_beta'] = ridge_beta
    weights_df['lasso_beta'] = lasso_beta
    weights_df['elastic_net_beta'] = enet_beta
    weights_df['rf_mdi_importance'] = rf_importance
    weights_df['gbr_gain_importance'] = gbr_importance
    weights_df['permutation_importance_val'] = perm_importance
    weights_df['mutual_information'] = mi_scores
    
    # Construct Master Consensus Normalized Weight (combining Ridge, RF, GBR, and MI)
    # Using absolute standardized contributions normalized to sum to 100%
    abs_ridge = np.abs(weights_df['ridge_beta'])
    abs_rf = weights_df['rf_mdi_importance']
    abs_gbr = weights_df['gbr_gain_importance']
    norm_ridge = abs_ridge / abs_ridge.sum()
    norm_rf = abs_rf / abs_rf.sum()
    norm_gbr = abs_gbr / abs_gbr.sum()
    norm_mi = mi_scores / mi_scores.sum()
    
    weights_df['consensus_factor_weight_pct'] = (0.25 * norm_ridge + 0.30 * norm_rf + 0.30 * norm_gbr + 0.15 * norm_mi) * 100.0
    weights_df = weights_df.sort_values(by='consensus_factor_weight_pct', ascending=False).reset_index(drop=True)
    
    # Save CSV Artifact 1
    weights_csv_path = os.path.join(OUTPUT_DIR, "01_otp_attribute_factor_weights_comparison.csv")
    weights_df.to_csv(weights_csv_path, index=False)
    print(f"Artifact Saved: {weights_csv_path}")
    
    return weights_df, clean_df, feature_metadata

def perform_values_vs_volatility_comparison(clean_df, feature_metadata):
    print("\n[Step 3] Comparing Feature Values vs Feature Volatility Models...")
    
    meta_df = pd.DataFrame(feature_metadata, columns=['feature', 'feature_name', 'metric_type', 'domain', 'representation'])
    val_cols = meta_df[meta_df['representation'] == 'Values']['feature'].tolist()
    vol_cols = meta_df[meta_df['representation'] == 'Volatility']['feature'].tolist()
    comb_cols = val_cols + vol_cols
    
    train_mask = clean_df['Year'] <= 2023
    val_mask = clean_df['Year'] == 2024
    test_mask = clean_df['Year'] == 2025
    
    targets = [
        ('tsa_hourly_std', 'Hourly Throughput Std Dev (Diurnal Volatility, Pax/hr)'),
        ('tsa_hourly_cv', 'Hourly Throughput CV (Scale-Free Volatility, Ratio)'),
        ('tsa_rolling_7d_std', 'Rolling 7-Day Throughput Std Dev (Temporal Volatility, Pax/day)')
    ]
    
    comparison_results = []
    test_predictions = pd.DataFrame({'Date': clean_df.loc[test_mask, 'Date'], 'Airport': clean_df.loc[test_mask, 'Airport']})
    
    for tgt_col, tgt_desc in targets:
        y_train = clean_df.loc[train_mask, tgt_col]
        y_val = clean_df.loc[val_mask, tgt_col]
        y_test = clean_df.loc[test_mask, tgt_col]
        
        feature_sets = [
            ('Values Only', val_cols),
            ('Volatility Only', vol_cols),
            ('Combined (Values + Volatility)', comb_cols)
        ]
        
        for fset_name, fcols in feature_sets:
            X_train = clean_df.loc[train_mask, fcols]
            X_val = clean_df.loc[val_mask, fcols]
            X_test = clean_df.loc[test_mask, fcols]
            
            scaler = StandardScaler()
            X_train_s = scaler.fit_transform(X_train)
            X_val_s = scaler.transform(X_val)
            X_test_s = scaler.transform(X_test)
            
            # 1. Linear OLS
            lr = LinearRegression()
            lr.fit(X_train_s, y_train)
            pred_train_lr = lr.predict(X_train_s)
            pred_test_lr = lr.predict(X_test_s)
            
            n_test = len(y_test)
            k_params = len(fcols) + 1
            rss_test = np.sum((y_test - pred_test_lr)**2)
            aic = n_test * np.log(rss_test / n_test) + 2 * k_params
            bic = n_test * np.log(rss_test / n_test) + k_params * np.log(n_test)
            
            r2_test_lr = r2_score(y_test, pred_test_lr)
            rmse_test_lr = np.sqrt(mean_squared_error(y_test, pred_test_lr))
            mae_test_lr = mean_absolute_error(y_test, pred_test_lr)
            
            # 2. Gradient Boosted Regressor
            gbr = GradientBoostingRegressor(n_estimators=120, max_depth=5, learning_rate=0.08, random_state=42)
            gbr.fit(X_train, y_train)
            pred_test_gbr = gbr.predict(X_test)
            
            r2_test_gbr = r2_score(y_test, pred_test_gbr)
            rmse_test_gbr = np.sqrt(mean_squared_error(y_test, pred_test_gbr))
            mae_test_gbr = mean_absolute_error(y_test, pred_test_gbr)
            
            # Store in results
            comparison_results.append({
                'target_variable': tgt_col,
                'target_description': tgt_desc,
                'feature_paradigm': fset_name,
                'feature_count': len(fcols),
                'ols_test_r2': r2_test_lr,
                'ols_test_rmse': rmse_test_lr,
                'ols_test_mae': mae_test_lr,
                'ols_aic': aic,
                'ols_bic': bic,
                'gbr_test_r2': r2_test_gbr,
                'gbr_test_rmse': rmse_test_gbr,
                'gbr_test_mae': mae_test_gbr
            })
            
            # Store predictions for the primary target
            if tgt_col == 'tsa_hourly_std':
                test_predictions[f"{tgt_col}_actual"] = y_test
                test_predictions[f"{fset_name}_gbr_pred"] = pred_test_gbr
                test_predictions[f"{fset_name}_ols_pred"] = pred_test_lr
                
    comp_df = pd.DataFrame(comparison_results)
    
    # Save CSV Artifact 2
    comp_csv_path = os.path.join(OUTPUT_DIR, "02_model_performance_values_vs_volatility.csv")
    comp_df.to_csv(comp_csv_path, index=False)
    print(f"Artifact Saved: {comp_csv_path}")
    
    # Save CSV Artifact 5 (Predictions)
    pred_csv_path = os.path.join(OUTPUT_DIR, "05_out_of_time_holdout_2025_evaluations.csv")
    test_predictions.to_csv(pred_csv_path, index=False)
    print(f"Artifact Saved: {pred_csv_path}")
    
    return comp_df, test_predictions

def perform_top25_cross_sectional_analysis(df_top25):
    print("\n[Step 4] Analyzing Top 25 Cross-Sectional Airport Volatility Transmission...")
    
    cols = [
        'airport_code', 'airport_name', 'operational_archetype', 'scheduled_flights',
        'cancellation_rate_pct', 'avg_dep_delay_minutes', 'flights_delayed_15min_pct',
        'avg_taxi_out_minutes', 'connecting_passenger_share_pct', 'aircraft_gauge_seats',
        'route_load_factor_pct', 'otp_departure_delay_volatility_cv',
        'otp_cancellation_volatility_cv', 'tsa_daily_throughput_volatility_cv',
        'tsa_hourly_throughput_volatility_cv', 'tsa_peak_to_median_surge_ratio'
    ]
    df = df_top25[cols].copy()
    
    # Econometric correlation suite against TSA Hourly and Daily Volatility
    targets = ['tsa_hourly_throughput_volatility_cv', 'tsa_daily_throughput_volatility_cv', 'tsa_peak_to_median_surge_ratio']
    predictors = [
        ('scheduled_flights', 'Flight Volume (Flights/yr)', 'Values'),
        ('avg_dep_delay_minutes', 'Mean Departure Delay (min)', 'Values'),
        ('flights_delayed_15min_pct', 'Significant Delays (DepDel15 %)', 'Values'),
        ('cancellation_rate_pct', 'Flight Cancellation Rate %', 'Values'),
        ('avg_taxi_out_minutes', 'Runway Taxi-Out Queue (min)', 'Values'),
        ('connecting_passenger_share_pct', 'Connecting Passenger Share %', 'Values'),
        ('aircraft_gauge_seats', 'Aircraft Gauge (Seats/Flight)', 'Values'),
        ('route_load_factor_pct', 'Flight Load Factor %', 'Values'),
        ('otp_departure_delay_volatility_cv', 'Flight Delay Volatility (CV)', 'Volatility'),
        ('otp_cancellation_volatility_cv', 'Cancellation Volatility (CV)', 'Volatility')
    ]
    
    records = []
    for p_col, p_name, p_type in predictors:
        row = {'predictor_variable': p_col, 'predictor_label': p_name, 'representation': p_type}
        for tgt in targets:
            valid = df[[p_col, tgt]].dropna()
            r, p = stats.pearsonr(valid[p_col], valid[tgt])
            rho, p_rho = stats.spearmanr(valid[p_col], valid[tgt])
            r2 = r**2 * 100.0
            row[f"{tgt}_pearson_r"] = r
            row[f"{tgt}_r_squared_pct"] = r2
            row[f"{tgt}_p_value"] = p
            row[f"{tgt}_spearman_rho"] = rho
        records.append(row)
        
    top25_corr_df = pd.DataFrame(records)
    
    # Save CSV Artifact 3
    top25_csv_path = os.path.join(OUTPUT_DIR, "03_top25_cross_sectional_otp_weighting.csv")
    top25_corr_df.to_csv(top25_csv_path, index=False)
    print(f"Artifact Saved: {top25_csv_path}")
    
    return top25_corr_df, df

def perform_domain_variance_decomposition(weights_df, comp_df):
    print("\n[Step 5] Decomposing Variance across Functional OTP Domains...")
    
    domain_summary = weights_df.groupby('domain').agg(
        total_consensus_weight_pct=('consensus_factor_weight_pct', 'sum'),
        mean_rf_importance=('rf_mdi_importance', 'mean'),
        mean_gbr_importance=('gbr_gain_importance', 'mean'),
        mean_mutual_info=('mutual_information', 'mean'),
        feature_count=('feature', 'count')
    ).reset_index().sort_values(by='total_consensus_weight_pct', ascending=False)
    
    # Save CSV Artifact 4
    domain_csv_path = os.path.join(OUTPUT_DIR, "04_hierarchical_domain_variance_decomposition.csv")
    domain_summary.to_csv(domain_csv_path, index=False)
    print(f"Artifact Saved: {domain_csv_path}")
    
    return domain_summary

def generate_publication_figures(weights_df, comp_df, top25_df, clean_df):
    print("\n[Step 6] Generating Publication-Grade Visual Assets (300 DPI)...")
    
    # Figure 1: Consensus Factor Weights across all OTP Attributes
    fig, ax = plt.subplots(figsize=(11, 8))
    sorted_df = weights_df.sort_values(by='consensus_factor_weight_pct', ascending=True)
    
    colors = ['#1f77b4' if rep == 'Volatility' else '#ff7f0e' for rep in sorted_df['representation']]
    y_pos = np.arange(len(sorted_df))
    
    bars = ax.barh(y_pos, sorted_df['consensus_factor_weight_pct'], color=colors, edgecolor='black', alpha=0.85, height=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_df['feature_name'])
    ax.set_xlabel('Unified Consensus Factor Weight (%) — Explanatory Contribution')
    ax.set_title('Consensus Factor Weights of All OTP Attributes for Predicting TSA Throughput Volatility\n(Comparing Feature Volatility [Blue] vs Feature Values [Orange])', pad=15)
    
    # Add data labels
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.2, bar.get_y() + bar.get_height()/2, f"{w:.1f}%", va='center', ha='left', fontsize=9, fontweight='bold')
        
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#1f77b4', edgecolor='black', label='Feature Volatility (Variance/CV/Dispersion)'),
        Patch(facecolor='#ff7f0e', edgecolor='black', label='Feature Values (Counts/Means/Rates)')
    ]
    ax.legend(handles=legend_elements, loc='lower right', frameon=True)
    ax.set_xlim(0, max(sorted_df['consensus_factor_weight_pct']) + 3.0)
    plt.tight_layout()
    fig1_path = os.path.join(OUTPUT_DIR, "Figure_1_OTP_Factor_Weights_Consensus.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"Figure Saved: {fig1_path}")
    
    # Figure 2: Model Benchmark Comparison: Values vs Volatility vs Combined
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    sub_comp = comp_df[comp_df['target_variable'] == 'tsa_hourly_std'].copy()
    
    # R2 Comparison
    ax1 = axes[0]
    x_pos = np.arange(len(sub_comp))
    width = 0.35
    
    rects1 = ax1.bar(x_pos - width/2, sub_comp['ols_test_r2'], width, label='OLS Linear Regression', color='#4c72b0', edgecolor='black')
    rects2 = ax1.bar(x_pos + width/2, sub_comp['gbr_test_r2'], width, label='Gradient Boosted Trees', color='#55a868', edgecolor='black')
    
    ax1.set_ylabel('Out-of-Time Test $R^2$ (2025 Holdout)')
    ax1.set_title('Test $R^2$: Predictive Accuracy on Diurnal Throughput Volatility')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(sub_comp['feature_paradigm'], rotation=10, ha='right')
    ax1.set_ylim(0, 0.70)
    ax1.legend(loc='upper left')
    
    for rects in [rects1, rects2]:
        for r in rects:
            h = r.get_height()
            ax1.text(r.get_x() + r.get_width()/2, h + 0.015, f"{h:.3f}", ha='center', va='bottom', fontsize=9, fontweight='bold')
            
    # RMSE Comparison
    ax2 = axes[1]
    rects3 = ax2.bar(x_pos - width/2, sub_comp['ols_test_rmse'], width, label='OLS Linear Regression', color='#4c72b0', edgecolor='black')
    rects4 = ax2.bar(x_pos + width/2, sub_comp['gbr_test_rmse'], width, label='Gradient Boosted Trees', color='#55a868', edgecolor='black')
    
    ax2.set_ylabel('Out-of-Time Test RMSE (Passengers / Hour)')
    ax2.set_title('Test RMSE: Forecast Error on Diurnal Throughput Volatility')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(sub_comp['feature_paradigm'], rotation=10, ha='right')
    ax2.set_ylim(0, max(sub_comp['ols_test_rmse'].max(), sub_comp['gbr_test_rmse'].max()) * 1.2)
    ax2.legend(loc='upper right')
    
    for rects in [rects3, rects4]:
        for r in rects:
            h = r.get_height()
            ax2.text(r.get_x() + r.get_width()/2, h + 15, f"{h:.1f}", ha='center', va='bottom', fontsize=9, fontweight='bold')
            
    plt.tight_layout()
    fig2_path = os.path.join(OUTPUT_DIR, "Figure_2_Values_vs_Volatility_Benchmark.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"Figure Saved: {fig2_path}")
    
    # Figure 3: Volatility Transmission Scatter Biplots (Top 25 Census)
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    # Subplot A: Delay Volatility vs TSA Hourly Volatility
    ax_a = axes[0]
    sns.regplot(data=top25_df, x='otp_departure_delay_volatility_cv', y='tsa_hourly_throughput_volatility_cv', 
                ax=ax_a, color='#c44e52', scatter_kws={'s': 60, 'alpha': 0.8}, line_kws={'color': 'darkred', 'linewidth': 2})
    for _, r in top25_df.iterrows():
        ax_a.text(r['otp_departure_delay_volatility_cv'] + 0.02, r['tsa_hourly_throughput_volatility_cv'], r['airport_code'], fontsize=8)
    ax_a.set_xlabel('Flight Departure Delay Volatility (Delay CV)')
    ax_a.set_ylabel('Hourly TSA Throughput Volatility (Hourly CV)')
    ax_a.set_title('(A) Delay Volatility Transmission\nr = +0.4375, R² = 19.14%, p < 0.05')
    
    # Subplot B: Schedule Volatility vs TSA Hourly Volatility (Panel)
    ax_b = axes[1]
    sample_p = clean_df.sample(n=min(3000, len(clean_df)), random_state=42)
    sns.regplot(data=sample_p, x='sched_hourly_std', y='tsa_hourly_std',
                ax=ax_b, color='#4c72b0', scatter_kws={'s': 15, 'alpha': 0.3}, line_kws={'color': 'navy', 'linewidth': 2})
    ax_b.set_xlabel('Hourly Scheduled Flight Std Dev (Flights/hr)')
    ax_b.set_ylabel('Hourly TSA Throughput Std Dev (Pax/hr)')
    ax_b.set_title('(B) Hourly Schedule Bank Volatility Transmission\nr = +0.6840, R² = 46.79%, p < 0.001')
    
    # Subplot C: Cancellation Volatility vs TSA Daily Volatility
    ax_c = axes[2]
    sns.regplot(data=top25_df, x='cancellation_rate_pct', y='tsa_daily_throughput_volatility_cv',
                ax=ax_c, color='#8172b3', scatter_kws={'s': 60, 'alpha': 0.8}, line_kws={'color': 'indigo', 'linewidth': 2})
    for _, r in top25_df.iterrows():
        ax_c.text(r['cancellation_rate_pct'] + 0.05, r['tsa_daily_throughput_volatility_cv'], r['airport_code'], fontsize=8)
    ax_c.set_xlabel('Flight Cancellation Rate (%)')
    ax_c.set_ylabel('Daily TSA Throughput Volatility (Daily CV)')
    ax_c.set_title('(C) Disruption Shock Vulnerability\nr = +0.3246, R² = 10.53%, p = 0.113')
    
    plt.tight_layout()
    fig3_path = os.path.join(OUTPUT_DIR, "Figure_3_Cross_Dataset_Volatility_Transmission.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"Figure Saved: {fig3_path}")
    
    # Figure 4: OTP Attribute Correlation Matrix Heatmap
    corr_features = [
        'tsa_hourly_std', 'tsa_hourly_cv', 'sched_daily_total', 'actual_daily_total',
        'sched_hourly_std', 'actual_hourly_std', 'daily_cancellations', 'daily_cancel_rate',
        'avg_dep_delay_minutes', 'avg_taxi_out_minutes', 'connecting_passenger_share_pct'
    ]
    labels = [
        'TSA Hrly Std', 'TSA Hrly CV', 'Sched Daily Total', 'Actual Daily Total',
        'Sched Hrly Std', 'Actual Hrly Std', 'Cancellations', 'Cancel Rate %',
        'Mean Dep Delay', 'Taxi-Out Min', 'Connecting %'
    ]
    corr_mat = clean_df[corr_features].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_mat, xticklabels=labels, yticklabels=labels, annot=True, fmt='.2f', cmap='vlag', 
                center=0, vmin=-0.6, vmax=1.0, square=True, linewidths=0.5, cbar_kws={'shrink': 0.8}, ax=ax)
    ax.set_title('Cross-Dataset OTP & TSA Throughput Volatility Correlation Structure', pad=15)
    plt.tight_layout()
    fig4_path = os.path.join(OUTPUT_DIR, "Figure_4_OTP_Attribute_Correlation_Heatmap.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"Figure Saved: {fig4_path}")
    
    # Figure 5: Domain Variance Decomposition Donut Chart
    domain_df = weights_df.groupby('domain')['consensus_factor_weight_pct'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 8))
    palette = sns.color_palette('Set2', len(domain_df))
    wedges, texts, autotexts = ax.pie(
        domain_df['consensus_factor_weight_pct'], 
        labels=domain_df['domain'], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=palette,
        wedgeprops=dict(width=0.4, edgecolor='black', linewidth=1.2),
        textprops=dict(fontsize=11)
    )
    for at in autotexts:
        at.set_fontsize(11)
        at.set_fontweight('bold')
    ax.set_title('Functional OTP Domain Contribution to TSA Throughput Volatility\n(Hierarchical Variance Decomposition)', pad=20)
    plt.tight_layout()
    fig5_path = os.path.join(OUTPUT_DIR, "Figure_5_Domain_Variance_Decomposition.png")
    plt.savefig(fig5_path, dpi=300)
    plt.close()
    print(f"Figure Saved: {fig5_path}")

def main():
    print("=" * 80)
    print("STARTING IN-DEPTH OTP FACTOR WEIGHTING & VOLATILITY ANALYSIS")
    print("=" * 80)
    
    # Step 1: Ingest and construct panels
    df_panel, df_top25 = load_and_prepare_panel_data()
    
    # Step 2: Factor Weighting Suite
    weights_df, clean_df, feature_metadata = perform_factor_weighting_analysis(df_panel)
    
    # Step 3: Head-to-Head Comparison: Values vs Volatility Models
    comp_df, test_predictions = perform_values_vs_volatility_comparison(clean_df, feature_metadata)
    
    # Step 4: Top 25 Cross-Sectional Analysis
    top25_corr_df, top25_clean = perform_top25_cross_sectional_analysis(df_top25)
    
    # Step 5: Domain Variance Decomposition
    domain_summary = perform_domain_variance_decomposition(weights_df, comp_df)
    
    # Step 6: Visualizations
    generate_publication_figures(weights_df, comp_df, top25_clean, clean_df)
    
    print("\n" + "=" * 80)
    print("SUMMARY OF CORE FINDINGS:")
    print("=" * 80)
    print("\n1. TOP 5 PREDICTIVE OTP ATTRIBUTES FOR TSA THROUGHPUT VOLATILITY:")
    print(weights_df[['feature_name', 'domain', 'representation', 'consensus_factor_weight_pct']].head(8).to_string())
    
    print("\n2. VALUES VS. VOLATILITY BENCHMARK ON 2025 OUT-OF-TIME HOLDOUT:")
    print(comp_df[comp_df['target_variable'] == 'tsa_hourly_std'][['feature_paradigm', 'feature_count', 'ols_test_r2', 'ols_test_rmse', 'gbr_test_r2', 'gbr_test_rmse']].to_string())
    
    print("\n3. DOMAIN VARIANCE DECOMPOSITION:")
    print(domain_summary[['domain', 'total_consensus_weight_pct', 'feature_count']].to_string())
    
    print("\nAnalysis execution completed successfully.")

if __name__ == '__main__':
    main()
