from sklearn import tree

class my_decission_tree():
    def __init__(self):
        self.clf = tree.DecisionTreeClassifier(random_state=0)
    def _fit(self,X, y):
        self.clf = self.clf.fit(X, y)
    def _predict(self,X):
        return self.clf.predict(X)