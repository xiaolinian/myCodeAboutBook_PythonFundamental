#chapter7 csvEx
##with open("price2016.csv","r") as f:
##    ls = []
##    for line in f:
##        line = line.replace("\n","")
##        ls.append(line.split(","))
##    print(ls)
##

fr = open("price2016.csv","r")
fw = open("price2016out.csv","w")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j].replace(".","").isnumeric():
            ls[i][j] = "{:.2f}%".format(float(ls[i][j])/100)

for row in ls:
    print(row)
    fw.write(",".join(row)+"\n")
fr.close()
fw.close()
