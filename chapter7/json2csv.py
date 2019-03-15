#e14.1json2csv.py
import json
fr = open("price2016.json","r")
ls = json.load(fr)
data = [ list(ls[0].keys()) ]
print(data)
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016json2csv.csv","w")
for x in data:
    fw.write(",".join(x)+"\n")
fw.close()        
    
