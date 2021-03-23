import random
import copy
import math

def MainFunc(x, y):
    return ((math.cos(x**2)) * (math.sin(y**2))) + (x + y)

#Individual

#Population

#kromosomosome [Binary]
def GenerateChro(ChroSize):
    kromosom = []
    for _ in range(ChroSize):
        kromosom.append(random.randint(0, 1))
    return kromosom

def GeneratePopu(PopuSize):
    Popu = []
    for _ in range(PopuSize):
        Popu.append(GenerateChro(10))
    return Popu

def DecodeBiner(kromosom):
    xMin, xMax, yMin, yMax = (-1, 2, -1, 1)

    x = xMin + (xMax - xMin / (2**-1 + 2**-2 + 2**-3 + 2**-4 + 2**-5)) * (kromosom[0] * 2**-1 + kromosom[1] * 2**-2 + kromosom[2] * 2**-3 + kromosom[3] * 2**-4 * kromosom[4] * 2**-5)
    y = yMin + (yMax - yMin / (2**-1 + 2**-2 + 2**-3 + 2**-4 + 2**-5)) * (kromosom[5] * 2**-1 + kromosom[6] * 2**-2 + kromosom[7] * 2**-3 + kromosom[8] * 2**-4 * kromosom[9] * 2**-5)

    return x, y

#Fitness
def HitungFitness(kromosom):
    x,y = DecodeBiner(kromosom)
    return MainFunc(x, y)

def HSFitness(populasi):
    SFitness = []

    for i in range(len(populasi)):
        tempFitness = HitungFitness(populasi[i])
        SFitness.append(tempFitness)

    return SFitness   

#Crossover [Two Point]

def Crossover(ayah, ibu, pc): 
    nilaiRandom = random.uniform(0, 1)
    if (nilaiRandom < pc):
        titik1 = random.randint(1, 7)
        print(titik1)
        titik2 = random.randint(titik1+1, 8)
        print(titik2)
        for i in range(0, titik1):
            ayah[i], ibu[i] = ibu[i], ayah[i]
        for i in range(titik1+1, titik2):
            ayah[i], ibu[i] = ibu[i], ayah[i]
        for i in range(titik2, 10, 1):
            ayah[i], ibu[i] = ibu[i], ayah[i]

    return ayah, ibu

a = GeneratePopu(2)
print(a)
print(Crossover(a[0], a[1], 1))

#Mutation

#Survivor Selection [Generational Replacement]

#Stopping Criteria [Time Limit]
