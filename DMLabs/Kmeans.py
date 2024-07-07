import numpy as np


class KMeans:
    def __init__(self, n_clusters, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters

    def fit(self, X):
        # Initialize centroids randomly
        centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iters):
            # Assign each data point to the nearest centroid
            labels = self._assign_labels(X, centroids)

            # Update centroids based on the mean of the data points assigned to them
            new_centroids = self._update_centroids(X, labels)

            # If centroids don't change much, stop
            if np.allclose(centroids, new_centroids):
                break

            centroids = new_centroids

        self.centroids = centroids
        self.labels = labels

    def _assign_labels(self, X, centroids):
        distances = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def _update_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for i in range(self.n_clusters):
            centroids[i] = X[labels == i].mean(axis=0)
        return centroids


# Example usage:
if __name__ == "__main__":
    # Generate some random data
    np.random.seed(0)
    X = np.random.randn(100, 2)

    # Initialize and fit KMeans
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    # Get centroids and labels
    centroids = kmeans.centroids
    labels = kmeans.labels

    print("Centroids:")
    print(centroids)
    print("Labels:")
    print(labels)
