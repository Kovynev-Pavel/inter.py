X = []
Y = []
class interpolyation:
    def add_in_list(self, a):
        for x, y in a.items():
            X.append(x)
            Y.append(y)
    def count_interpolyation(self, iks):
        for i in range(1, len(X)):
            if X[i - 1] <= iks <= X[i]:
                igrek = (Y[i] - Y[i - 1]) / (X[i] - X[i - 1]) * (iks - X[i - 1]) + Y[i - 1]
                return igrek



