lis1 = [1, 2, 3, 4, 5]
lis2 = [5, 6, 7, 8, 9]
found_common = False
for element in lis1:
    if element in lis2:
        found_common = True
        break
if found_common:
    print(True)
else:
    print(False)