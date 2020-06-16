# Chapter 6 practice project
tableData = [['apples', 'orages', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
colWidths = [0] * len(tableData)

for x in range(len(tableData)):
    for y in range(len(tableData[x])):
        width = int(len(tableData[x][y]))
        if width > colWidths[x]:
            colWidths[x] = width

def printTable():
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidths[x]),end=' ')
        print()

printTable() 
