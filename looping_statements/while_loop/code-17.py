# TODO Try Such Kind of Examples
w = [1,2,3,4,5,["hi",90,34,123],900,123,9+4j]
i = 0

while i < len(w): #
    if isinstance(w[i] , list):
        x = w.pop(i) # x = w.pop(5)  | ["hi",90,34,123]
        y = w + x
        print(y)

    i+=1

