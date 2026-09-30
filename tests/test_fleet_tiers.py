"""
tests/test_fleet_tiers.py
-------------------------
Unit tests for REC-04 High-Cardinality Airframe Gauge Tiering.
"""

import unittest
import pandas as pd
from src.features.fleet_tiers import assign_fleet_gauge_tier, apply_fleet_tiering

class TestFleetTiers(unittest.TestCase):
    def test_tier_assignment(self):
        self.assertEqual(assign_fleet_gauge_tier(50), "Regional")
        self.assertEqual(assign_fleet_gauge_tier(76), "Regional")
        self.assertEqual(assign_fleet_gauge_tier(77), "Narrowbody")
        self.assertEqual(assign_fleet_gauge_tier(180), "Narrowbody")
        self.assertEqual(assign_fleet_gauge_tier(210), "Narrowbody")
        self.assertEqual(assign_fleet_gauge_tier(211), "Widebody")
        self.assertEqual(assign_fleet_gauge_tier(350), "Widebody")

    def test_apply_fleet_tiering_columns(self):
        df = pd.DataFrame({"Scheduled_Seats": [70, 160, 280]})
        out = apply_fleet_tiering(df)
        self.assertIn("gauge_tier", out.columns)
        self.assertIn("gauge_modal_lead_min", out.columns)
        self.assertIn("is_regional", out.columns)
        self.assertIn("is_narrowbody", out.columns)
        self.assertIn("is_widebody", out.columns)
        
        # Widebody modal lead must be 140 min
        self.assertEqual(out["gauge_modal_lead_min"].iloc[2], 140)
        # Regional modal lead must be 55 min
        self.assertEqual(out["gauge_modal_lead_min"].iloc[0], 55)

if __name__ == "__main__":
    unittest.main()
