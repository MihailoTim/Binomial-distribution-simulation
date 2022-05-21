import random

while True:
    try:
        numberOfSimulations = int(input('Enter the number of simulations:'))
        if(numberOfSimulations<=0):
            print("Enter a positive number.")
            continue
        else:
            break
    except:
        print("Enter an integer.")
        continue

while True:
    try:
        numberOfExperiments = int(input('Enter the number of experiments:'))
        if(numberOfExperiments<=0):
            print("Enter a positive number.")
            continue
        else:
            break
    except:
        print("Enter an integer.")
        continue

while True:
    try:
        numberOfShots = int(input('Enter the number of shots:'))
        if(numberOfShots<=0):
            print("Enter a positive number.")
            continue
        else:
            break
    except:
        print("Enter an integer.")
        continue

while True:
    try:
        hitProbability  = float(input('Enter the probability of a hit: '))
        if(0 <= hitProbability <= 1):
            break
        else:
            print("A number from [0,1] is needed.")
            continue
    except:
        print("Enter a float.")
        continue


numberOfHits = [0 for i in range(11)]

totalNumberOfExperiments = numberOfSimulations * numberOfExperiments

for simulation in range(numberOfSimulations):
    for experiment in range(numberOfExperiments):
        hitCount = 0
        for shot in range(numberOfShots):
            x=random.random()
            if(x<=hitProbability):
                hitCount+=1
        numberOfHits[hitCount]+=1

expectedNumberOfHits = 0

for i in range(0,11):
    expectedNumberOfHits += i * numberOfHits[i]/totalNumberOfExperiments
    txt = "Number of hits: {:<8} Frequency: {:<8} Probability: {:.5f}"
    print(txt.format(i, numberOfHits[i], numberOfHits[i]/totalNumberOfExperiments))

print("\nExcpected number of hits: " + str(expectedNumberOfHits).format(":.6f"))



