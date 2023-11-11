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
inter1 = interpolyation()
inter1.add_in_list({3: 1, 4: 2, 5: 4})
inter1.count_interpolyation(3.2)

