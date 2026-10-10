"""
Feature Engineering and Deconvolution Modules.
"""
from .time_features import generate_temporal_features
from .fleet_tiers import apply_fleet_tiering, assign_fleet_gauge_tier
from .demand_deflat import compute_originating_demand, get_connecting_ratio, get_originating_multiplier
from .cluster_adapt import convolve_cluster_adaptive_demand, compute_cluster_weights
from .airside_flow import compute_airside_interactions
from .checkpoint_map import compute_checkpoint_weights, get_checkpoint_confidence
from .feature_pipeline import build_conformed_feature_matrix

__all__ = [
    # Modern Feature Engineering Pipeline (REC-01 to REC-13)
    "generate_temporal_features",
    "apply_fleet_tiering",
    "assign_fleet_gauge_tier",
    "compute_originating_demand",
    "get_connecting_ratio",
    "get_originating_multiplier",
    "convolve_cluster_adaptive_demand",
    "compute_cluster_weights",
    "compute_airside_interactions",
    "compute_checkpoint_weights",
    "get_checkpoint_confidence",
    "build_conformed_feature_matrix",
]

