import numpy as np

australian = np.loadtxt("dane/australian.txt", dtype="str")
australianType = np.loadtxt("dane/australian-type.txt", dtype="str")
infoData = np.loadtxt("dane/_info-data-discrete.txt", dtype="str")

# print(australian)
# print(australianType)

# print("\n3b\n")
# x, y = np.where(infoData == "australian")
# print(f"wielkosc klas decyzyjnych = {infoData[int(x)][2]}")

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

# print("\n3f\n")
# x1, y1 = np.where(australianType == "n")
# wholeSystem = np.array([])
# for i in x1:
#     tym = np.array(australian[:, i], dtype='float')
#     wholeSystem = np.append(wholeSystem, tym)
#     print(f"{australianType[i][0]}: std = {np.std(tym)}")
# print(f"Whole system: std = {np.std(wholeSystem)}")

print("\n4a\n")
x1, y1 = np.where(australianType == "n")
for i in x1:
    tym = np.array(australian[:, i], dtype='float')
    print(tym)
    pass