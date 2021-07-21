import numpy as np

class KMeans:
    def __init__(self, k=2, eps=0.001, max_iter=300):
        self.k = k
        self.eps = eps
        self.max_iter = max_iter
        self.centroids = {}
        self.classifications = {}

    def fit(self, data):
        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []
            
            for datapoint in data:
                distances = [np.linalg.norm(datapoint - self.centroids[j]) for j in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(datapoint)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            early_stop = True
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100) > self.eps:
                        early_stop = False

            if early_stop:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[j]) for j in self.centroids]
        return distances.index(min(distances))

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    X = np.array(
        [[1, 2],
        [1.5, 2.8],
        [7, 9],
        [6, 8],
        [0.5, 1.5],
        [9, 11]]
    )

    clf = KMeans()
    clf.fit(X)

    f = plt.figure(figsize=(20, 10))
    # plt.scatter(X[:,0], X[:, 1], s=200)
    for centroid in clf.centroids:
        plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker="+", color="red", s=300)
    
    colors = ["green", "blue"]
    for classification in clf.classifications:
        color = colors[classification]
        for datapoint in clf.classifications[classification]:
            plt.scatter(datapoint[0], datapoint[1], marker="o", color=color, s=200)
    
    plt.show()
