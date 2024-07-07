import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, KDTree


class KNNVoronoiKDTree:
    def __init__(self, points):
        self.points = np.array(points)
        self.kd_tree = KDTree(self.points)
        self.voronoi = Voronoi(self.points)

    def query(self, query_point, k=1):
        # Find the Voronoi region of the query point
        region_index = self.voronoi.point_region[self.kd_tree.query(query_point)[1]]

        # Get the vertices of the Voronoi region
        region_vertices = np.array([self.voronoi.vertices[i] for i in self.voronoi.regions[region_index] if i != -1])

        # Find the nearest neighbors within the Voronoi region using kd-tree
        neighbors_indices = self.kd_tree.query(query_point, k=k)[1]

        # Calculate distances from the query point to the neighbors
        distances = np.linalg.norm(self.points[neighbors_indices] - query_point, axis=1)

        # Return the nearest neighbors and their distances
        return self.points[neighbors_indices], distances

    def plot_voronoi(self):
        voronoi_plot_2d(self.voronoi)
        plt.scatter(self.points[:, 0], self.points[:, 1], c='red', marker='o', label='Data Points')
        plt.title('Voronoi Diagram with Data Points')
        plt.legend()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Generate random data points
    np.random.seed(42)
    data_points = np.random.rand(10, 2)

    # Create KNNVoronoiKDTree object
    knn_voronoi_kd_tree = KNNVoronoiKDTree(data_points)

    # Plot Voronoi diagram with data points
    knn_voronoi_kd_tree.plot_voronoi()

    # Query for nearest neighbors
    query_point = np.array([0.5, 0.5])
    k_neighbors, distances = knn_voronoi_kd_tree.query(query_point, k=3)

    # Print results
    print("Query Point:", query_point)
    print("Nearest Neighbors:", k_neighbors)
    print("Distances:", distances)
