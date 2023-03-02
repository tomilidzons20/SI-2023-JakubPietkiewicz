import numpy as np

australian = np.loadtxt("dane/australian.txt", dtype="str")
australianType = np.loadtxt("dane/australian-type.txt", dtype="str")
infoData = np.loadtxt("dane/_info-data-discrete.txt", dtype="str")

# print(australian)
# print(australianType)

# print("\n3b\n")
# x, y = np.where(infoData == "australian")
# print(f"wielkosc klas decyzyjnych = {infoData[int(x)][2]}")
#
# print("\n3c\n")
# x1, y1 = np.where(australianType == "n")
# for i in x1:
#     tym = np.array(australian[:, i], dtype='float')
#     max = np.max(tym)
#     min = np.min(tym)
#     print(f"{australianType[i][0]}: max = {max}, min = {min}")
#
# print("\n3d\n")
# for i in range(len(australian[0]) - 1):
#     print(f"{australianType[i][0]}: uniqueAttributes = {len(np.unique(australian[:, i]))}")
#
# print("\n3e\n")
# for i in range(len(australian[0]) - 1):
#     print(f"{australianType[i][0]}: uniqueAttributes = {np.unique(australian[:, i])}")
#
# print("\n3f\n")
# x1, y1 = np.where(australianType == "n")
# wholeSystem = np.array([])
# for i in x1:
#     tym = np.array(australian[:, i], dtype='float')
#     wholeSystem = np.append(wholeSystem, tym)
#     print(f"{australianType[i][0]}: std = {np.std(tym)}")
# print(f"Whole system: std = {np.std(wholeSystem)}")

print("\n4a\n")

# srednie kolumn z n
x1, y1 = np.where(australianType == "n")
tab1 = np.zeros(shape=14)
for i in x1:
    tab1[i] = np.mean(np.array(australian[:, i], dtype='float')).round(2)

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
australian[dataChoice] = "?"

# zapisanie tabeli przed i po wypelnieniu znakow "?" wartosciami srednimi i najczesciej wystepujacymi symbolami
np.savetxt("file1.txt", australian, fmt="%s")

for i in x1:
    tym = australian[:, i]
    tym[tym == "?"] = tab1[i]

for i in x2:
    tym = australian[:, i]
    tym[tym == "?"] = int(tab2[i])

np.savetxt("file2.txt", australian, fmt="%s")