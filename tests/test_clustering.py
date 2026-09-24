import unittest
import pandas as pd
from etl.perform_top25_clustering import run_top25_clustering

class TestTop25Clustering(unittest.TestCase):
    def test_top25_clustering_output_shape(self):
        """Verify Top 25 clustering produces exactly 25 candidate airfields and expected schema."""
        df = run_top25_clustering()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 25)
        self.assertIn("airport", df.columns)
        self.assertIn("cluster", df.columns)
        self.assertIn("cluster_archetype", df.columns)

    def test_top25_clustering_clusters(self):
        """Verify all 4 operational clusters are assigned."""
        df = run_top25_clustering()
        clusters = set(df["cluster"].unique())
        self.assertEqual(len(clusters), 4)
        archetypes = set(df["cluster_archetype"].unique())
        self.assertIn("Mega-Connecting Gateways", archetypes)

if __name__ == "__main__":
    unittest.main()
