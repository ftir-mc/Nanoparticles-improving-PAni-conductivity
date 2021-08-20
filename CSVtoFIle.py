import csv

with open('TR.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#print(data)


for i in range (1,len(data)):
    year=(str(data[i][0]))
    title=(str(data[i][1]))
    name=(str(year)+"-"+str(title)+".txt")
    g=open(name, "w")
    g.write(str(data[i][2]))
    g.close()
