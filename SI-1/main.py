import numpy as np

australian = np.loadtxt("../dane/australian.txt", dtype="str")
australianType = np.loadtxt("../dane/australian-type.txt", dtype="str")
infoData = np.loadtxt("../dane/_info-data-discrete.txt", dtype="str")

# Zad 3a ==============================================================
print("\n3a\n")
# print(australian)
# print(australianType)

# Zad 3b ==============================================================
print("\n3b\n")
x, y = np.where(infoData == "australian")
decisionClassSize = int(infoData[int(x)][2])
print(f"wielkosc klas decyzyjnych = {decisionClassSize}")

# Zad 3c ==============================================================
print("\n3c\n")
x1, y1 = np.where(australianType == "n")
for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    max1 = np.max(tym)
    min1 = np.min(tym)
    print(f"{australianType[i][0]}: max = {max1}, min = {min1}")

# Zad 3d ==============================================================
print("\n3d\n")
for i in range(len(australian[0]) - 1):
    print(f"{australianType[i][0]}: uniqueAttributes = {len(np.unique(australian[:, i]))}")

# Zad 3e ==============================================================
print("\n3e\n")
for i in range(len(australian[0]) - 1):
    print(f"{australianType[i][0]}: uniqueAttributes = {np.unique(australian[:, i])}")

# Zad 3f ==============================================================
print("\n3f\n")
x1, y1 = np.where(australianType == "n")
wholeSystem = np.array([])
for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    wholeSystem = np.append(wholeSystem, tym)
    print(f"{australianType[i][0]}: std = {np.std(tym)}")
print(f"Whole system: std = {np.std(wholeSystem)}")

# Zad 4a ==============================================================
print("\n4a\n")

# srednie kolumn z n
x1, y1 = np.where(australianType == "n")
tab1 = np.zeros(shape=14)
for i in x1:
    tab1[i] = np.mean(np.array(australian[:, i], dtype='float'))

# print(f"{tab1}\n")

# najczesciej wystepujace w kolumnie z s
x2, y2 = np.where(australianType == "s")
tab2 = np.zeros(shape=14)
for i in x2:
    unique, counts = np.unique(australian[:, i], return_counts=True)
    tab2[i] = unique[np.argmax(counts)]

# print(f"{tab2}\n")

# wypelnienie 10% tabeli znakami "?"
dataChoice = np.random.choice([True, False], size=australian.shape, p=[0.1, 0.9])
dataChoice[:, -1] = False
australian[dataChoice] = "?"


# zapisanie tabeli przed wypelnieniem znakow "?"
# wartosciami srednimi i najczesciej wystepujacymi symbolami
# w celu kontroli poprawnosci wykonania zadania
np.savetxt("file1.txt", australian, fmt="%s")

# zamiana znakow "?" na srednie kolumn
for i in x1:
    tym = australian[:, i]
    tym[tym == "?"] = tab1[i]

# zamiana znakow "?" na najczesciej wystepujace atrybuty w kolumnie
for i in x2:
    tym = australian[:, i]
    tym[tym == "?"] = int(tab2[i])

# zapisanie tabeli po wypielnieniu znakow "?"
np.savetxt("file2.txt", australian, fmt="%s")

# Zad 4b ==============================================================
print("\n4b\n")


# funkcja normalizujaca atrybut do przedzialu
def interval_calc(a, b, mina, maxa, aiobj):
    nominator = (float(aiobj) - minai) * (b - a)
    denominator = maxa - mina
    res = nominator / denominator + a
    return str(res)


x1, y1 = np.where(australianType == "n")

for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    minai = np.min(tym)
    maxai = np.max(tym)
    for j in range(decisionClassSize):
        australian[j, i] = interval_calc(0, 1, minai, maxai, australian[j, i])

np.savetxt("file3.txt", australian, fmt="%s")

# Zad 4c ==============================================================
print("\n4c\n")


# funckja obliczajaca standaryzacje
def standarization_calc(mean, variance, aiobj):
    res = (float(aiobj) - mean) / variance
    return str(res)


x1, y1 = np.where(australianType == "n")

# wzor na variance jest w zadaniu nieprawidlowy poniewaz brakuje w nim podzielenia calosci przez number_of_objects
# dlatego skorzystałem z funkcji wbudowanej w numpy
# dodatkowo wykorzystałem wzor na srednia z numpy
for i in x1:
    meanai = np.mean(np.array(australian[:, i], dtype='float'))
    varianceai = np.var(np.array(australian[:, i], dtype='float'))
    for j in range(decisionClassSize):
        australian[j, i] = standarization_calc(meanai, varianceai, australian[j, i])

np.savetxt("file4.txt", australian, fmt="%s")

# Zad 4d ==============================================================
print("\n4d\n")

# wczytanie csv jako np.array
data = np.loadtxt("../dane/Churn_Modelling.csv", delimiter=",", dtype="str")
# usuniecie wiersza z podpisami kolumn
data1 = np.delete(data, 0, axis=0)

# wybranie kolumny geography i unikatowych elementow
geography = data1[:, 4]
uniqueAttributes = np.unique(geography)
dummyVariables = []

# stworzenie dummy variables
for i, j in enumerate(uniqueAttributes):
    dummyVariables.append(np.where(geography == j, "1", "0").tolist())
dummyVariables = np.asarray(dummyVariables)

# dodanie kolumn w miejsce kolumny geography
tempData = data1[:, 0:4]
tempData = np.insert(tempData, 4, dummyVariables[1], axis=1)
tempData = np.insert(tempData, 5, dummyVariables[2], axis=1)
tempData = np.append(tempData, data1[:, 5:], axis=1)

# uzupelnienie rzedu z nazwami o dummy variables
nameRow = data[0, :4]
nameRow = np.insert(nameRow, 4, ["Geography.symbol2", "Geography.symbol3"], axis=0)
nameRow = np.append(nameRow, data[0, 5:], axis=0)

# dodanie rzedu z nazwami do tabeli
tempData = np.insert(tempData, 0, nameRow, axis=0)

# zapisanie pliku csv po zmianach
np.savetxt("zad4d.csv", tempData, delimiter=",", fmt="%s")
