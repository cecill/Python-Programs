def printIterates(OneDMap, initialConditions, nIterates):
    x=initialConditions
    for i in range(nIterates):
        x=OneDMap(x)
        print i, x

def LogisticMap(x):
    return 4.0 * x * (1.0 - x)

printIterates(LogisticMap, 0.3, 10)

raw_input('Press Enter to continue')