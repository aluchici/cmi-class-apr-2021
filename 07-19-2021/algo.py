from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np 
import pickle

# develop a model 
# wrap model into a class 
# expose model as a REST API
class BreastCancerClassifier:

    def __init__(self, min_score: float = 0.90, data: pd.DataFrame = None, target_column: str = None, 
    X: pd.DataFrame = None, y: pd.DataFrame = None):
        self.__data = data # data needs to be a Pandas DF
        self.__target_column = target_column
        self.__clf = KNeighborsClassifier(n_neighbors=10)
        self.__X = X
        self.__y = y
        self.__min_score = min_score

    @property
    def X(self):
        if self.__X is None and self.__y is not None:
            self.__X = self.__data.drop(self.__target_column)
        elif self.__X is None and self.__y is None:
            self.__y = self.__data[self.__target_column]
            self.__X = self.__data.drop(self.__target_column)
        return self.__X

    @property
    def y(self):
        if self.__y is None:
            self.__y = self.__data[self.__target_column]
        return self.__y

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.25)
        self.__clf = self.__clf.fit(X_train, y_train)
        score = self.__clf.score(X_test, y_test)
        print(f"Test score: %s" % score)
        if score < self.__min_score:
            raise Exception("Model test score below min threshold. Please try again.")

    def save(self, output: str = "sample"):
        if self.__clf:
            pickle.dump(self.__clf, open(output, "wb"))
        else:
            raise Exception("Invalid model. Please train a model before saving.")

    def load_model(self, input: str = "sample"):
        try:
            self.__clf = pickle.load(open(input, "rb"))
        except Exception as e:
            raise e

    def predict(self, X):
        return self.__clf.predict(X)[0]

    def load_X(self, X):
        self.__X = X
        return self

    def load_y(self, y):
        self.__y = y
        return self

    def load_data(self, data, target_column):
        self.__data = data
        self.__target_column = target_column
        return self

    def load_target_column(self, target_column):
        self.__target_column = target_column
        return self

class BreastCancerClassifierPreTrained:
    def __init__(self):
        self.clf = None 

    def load_model(self, input_file: str):
        self.clf = pickle.load(open(input_file, "rb"))


if __name__ == "__main__":
    data = load_breast_cancer(as_frame=True)
    X = data['data']
    y = data['target']
    X_new = X.loc[0]
    y_new = y.loc[0]
    X = X.loc[range(1, len(X))]
    y = y.loc[range(1, len(y))]

    # unable_to_train = 0
    # for i in range(25):
    #     clf = BreastCancerClassifier(min_score=0.91).load_X(X).load_y(y)
    #     try:
    #         clf.train()
    #         prediction = clf.predict(np.asarray(X_new).reshape(1, -1))
    #         print(f"Predicted tumor type: {prediction}; Actual tumor type: {y_new}")
    #     except Exception as e:
    #         print("Unable to train a model. Please try again later.")
    #         unable_to_train += 1
    # print(f"Failed to train model {unable_to_train} times.")
    # print("Bye!")

    # clf1 = BreastCancerClassifier().load_X(X).load_y(y)
    # clf1.train()
    # clf1.save("sample1")

    # clf2 = BreastCancerClassifier()
    # clf2.load_model("sample1")

    # pred1 = clf1.predict(np.asarray(X_new).reshape(1, -1))
    # pred2 = clf2.predict(np.asarray(X_new).reshape(1, -1))

    # print(f"First prediction {pred1}. Second prediction {pred2}")

    clf = BreastCancerClassifierPreTrained()
    clf.load_model("sample1")
    print(clf.clf.predict(np.asarray(X_new).reshape(1, -1)))
