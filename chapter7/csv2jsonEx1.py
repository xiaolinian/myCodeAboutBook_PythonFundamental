#e14.1csv2json.py
import json
fr = open("price2016.csv","r")
ls = []
lst = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()
print(ls)
fw = open("price2016.json","w")
for i in range(1,len(ls)):
    lst.append(dict(zip(ls[0],ls[i])))
print(lst)
json.dump(lst[:],fw,sort_keys=True,indent=4)
fw.close()
