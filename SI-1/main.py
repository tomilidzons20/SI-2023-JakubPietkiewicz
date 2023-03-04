import numpy as np

australian = np.loadtxt("../dane/australian.txt", dtype="str")
australian_type = np.loadtxt("../dane/australian-type.txt", dtype="str")
info_data = np.loadtxt("../dane/_info-data-discrete.txt", dtype="str")

# Zad 3a ==============================================================
print("\n3a\n")
# print(australian)
# print(australian_type)

# Zad 3b ==============================================================
print("\n3b\n")
x, y = np.where(info_data == "australian")
decision_class_size = int(info_data[int(x)][2])
print(f"wielkosc klas decyzyjnych = {decision_class_size}")

# Zad 3c ==============================================================
print("\n3c\n")
x1, y1 = np.where(australian_type == "n")
for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    max1 = np.max(tym)
    min1 = np.min(tym)
    print(f"{australian_type[i][0]}: max = {max1}, min = {min1}")

# Zad 3d ==============================================================
print("\n3d\n")
for i in range(len(australian[0]) - 1):
    print(f"{australian_type[i][0]}: unique_attributes = {len(np.unique(australian[:, i]))}")

# Zad 3e ==============================================================
print("\n3e\n")
for i in range(len(australian[0]) - 1):
    print(f"{australian_type[i][0]}: unique_attributes = {np.unique(australian[:, i])}")

# Zad 3f ==============================================================
print("\n3f\n")
x1, y1 = np.where(australian_type == "n")
whole_system = np.array([])
for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    whole_system = np.append(whole_system, tym)
    print(f"{australian_type[i][0]}: std = {np.std(tym)}")
print(f"Whole system: std = {np.std(whole_system)}")

# Zad 4a ==============================================================
print("\n4a\n")

# srednie kolumn z n
x1, y1 = np.where(australian_type == "n")
tab1 = np.zeros(shape=14)
for i in x1:
    tab1[i] = np.mean(np.array(australian[:, i], dtype='float'))

# print(f"{tab1}\n")

# najczesciej wystepujace w kolumnie z s
x2, y2 = np.where(australian_type == "s")
tab2 = np.zeros(shape=14)
for i in x2:
    unique, counts = np.unique(australian[:, i], return_counts=True)
    tab2[i] = unique[np.argmax(counts)]

# print(f"{tab2}\n")

# wypelnienie 10% tabeli znakami "?"
data_choice = np.random.choice([True, False], size=australian.shape, p=[0.1, 0.9])
data_choice[:, -1] = False
australian[data_choice] = "?"


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


x1, y1 = np.where(australian_type == "n")

for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    minai = np.min(tym)
    maxai = np.max(tym)
    for j in range(decision_class_size):
        australian[j, i] = interval_calc(0, 1, minai, maxai, australian[j, i])

np.savetxt("file3.txt", australian, fmt="%s")

# Zad 4c ==============================================================
print("\n4c\n")


# funckja obliczajaca standaryzacje
def standarization_calc(mean, variance, aiobj):
    res = (float(aiobj) - mean) / variance
    return str(res)


x1, y1 = np.where(australian_type == "n")

# wzor na variance jest w zadaniu nieprawidlowy poniewaz brakuje w nim podzielenia calosci przez number_of_objects
# dlatego skorzystałem z funkcji wbudowanej w numpy
# dodatkowo wykorzystałem wzor na srednia z numpy
for i in x1:
    meanai = np.mean(np.array(australian[:, i], dtype='float'))
    varianceai = np.var(np.array(australian[:, i], dtype='float'))
    for j in range(decision_class_size):
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
unique_attributes = np.unique(geography)
dummy_variables = []

# stworzenie dummy variables
for i, j in enumerate(unique_attributes):
    dummy_variables.append(np.where(geography == j, "1", "0").tolist())
dummy_variables = np.asarray(dummy_variables)

# dodanie kolumn w miejsce kolumny geography
temp_data = data1[:, 0:4]
temp_data = np.insert(temp_data, 4, dummy_variables[1], axis=1)
temp_data = np.insert(temp_data, 5, dummy_variables[2], axis=1)
temp_data = np.append(temp_data, data1[:, 5:], axis=1)

# uzupelnienie rzedu z nazwami o dummy variables
name_row = data[0, :4]
name_row = np.insert(name_row, 4, ["Geography.symbol2", "Geography.symbol3"], axis=0)
name_row = np.append(name_row, data[0, 5:], axis=0)

# dodanie rzedu z nazwami do tabeli
temp_data = np.insert(temp_data, 0, name_row, axis=0)

# zapisanie pliku csv po zmianach
np.savetxt("zad4d.csv", temp_data, delimiter=",", fmt="%s")
