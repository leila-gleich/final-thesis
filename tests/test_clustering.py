import os
import sys
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from etl.perform_top25_clustering import run_top25_clustering, get_pca_loadings_df


class TestTop25Clustering(unittest.TestCase):
    def test_top25_clustering_output_shape(self):
        """Verify Top 25 clustering produces exactly 25 candidate airfields and expected schema."""
        df = run_top25_clustering()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 25)
        self.assertIn("airport", df.columns)
        self.assertIn("cluster", df.columns)
        self.assertIn("cluster_archetype", df.columns)
        self.assertIn("PC1", df.columns)
        self.assertIn("PC2", df.columns)
        self.assertIn("PC3", df.columns)

    def test_top25_clustering_clusters(self):
        """Verify all 4 operational clusters are assigned."""
        df = run_top25_clustering()
        clusters = set(df["cluster"].unique())
        self.assertEqual(len(clusters), 4)
        archetypes = set(df["cluster_archetype"].unique())
        self.assertIn("Mega-Connecting Gateways", archetypes)

    def test_pca_loadings(self):
        """Verify PCA factor loadings are calculated across the 9 standardized operational metrics."""
        loadings = get_pca_loadings_df()
        self.assertIsInstance(loadings, pd.DataFrame)
        self.assertEqual(loadings.shape, (9, 3))
        self.assertEqual(list(loadings.columns), ["PC1", "PC2", "PC3"])

if __name__ == "__main__":
    unittest.main()
