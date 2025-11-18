input_str = input("Nhập X, Y cách nhau bởi dấu phẩy: ")
dimension=[int(x) for x in input_str.split(',')]
rowNums=dimension[0]
colNums=dimension[1]
multilist = [[0 for col in range(colNums)] for row in range(rowNums)]
for row in range(rowNums):
    for col in range(colNums):
        multilist[row][col] = row * col
        print(multilist[row][col], end=" ")