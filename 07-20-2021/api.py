from flask import Flask, request
from flask_restful import Resource, Api
import numpy as np 
from app import KMeans

app = Flask(__name__)
api = Api(app)


class KMeansClustering(Resource):
    def post(self):
        """
        request: 
        {
            "data": [[1,2], [2,3]],
            "k": 2
        }
        response: {
            "result": {
                1: [],
                2: []
            }
        }
        """
        data = np.asarray(request.json['data'])
        k = request.json['k']
        clf = KMeans(k=k)
        clf.fit(data)
        centroids = {}
        for c in clf.centroids:
            centroids[c] = list(clf.centroids[c])
        return {'result': centroids}


api.add_resource(KMeansClustering, "/cluster-data")

if __name__ == "__main__":
    app.run(debug=True)