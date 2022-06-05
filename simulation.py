from ast import Pow
import random

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

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


numberOfHits = [0 for i in range(numberOfShots+1)]

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

for i in range(0,numberOfShots+1):
    expectedNumberOfHits += i * numberOfHits[i]/totalNumberOfExperiments
    txt = "Number of hits: {:<8} Frequency: {:<8} Probability: {:.5f}"
    print(txt.format(i, numberOfHits[i], numberOfHits[i]/totalNumberOfExperiments))

print("\nExcpected number of hits: " + str(expectedNumberOfHits).format(":.6f"))



print("\nNow showing results from binomial distribution formula. Delta shows absolute difference between calculated and simulated values\n")

#don't mind the efficency of calculating factorial or power 
#that was not the point of this simulation

for i in range(0,numberOfShots+1):
    probability = factorial(numberOfShots)/(factorial(numberOfShots-i) * factorial(i)) * pow(hitProbability, i) * pow(1-hitProbability, numberOfShots-i)
    txt = "Number of hits: {:<8} Probability: {:.5f}         Delta {:.5f}"
    print(txt.format(i, probability, abs(probability - numberOfHits[i]/totalNumberOfExperiments)))