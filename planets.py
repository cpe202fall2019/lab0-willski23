def weight_on_planets():
    # takes weight as float variable
    weight = float(input("What do you weigh on earth? "))
    # calculates and prints weight for Mars and Jupiter
    print('\nOn Mars you would weigh ' + str(weight * .38) + " pounds.\nOn Jupiter you would weigh " + str
    (weight * 2.34) + " pounds.")


if __name__ == '__main__':
    weight_on_planets()
