#e7.1
"""
python源文件改写。编写一个程序，读取一个Python源程序文件，将文件中所有除保留字外的
小写字母换成大写字母，生成后的文件要能够被Python解析器正确执行。
"""
import keyword
s = keyword.kwlist

fr = open("json2csv.py","r")
str = fr.readlines()
print(str)
ls = []
for line in str:
    print(line)
    line = line.split()
    print(line)
    ls.append(line)
print(ls) #######

fo = open("file2save.py","w+")
for i in range(len(ls)):
    if str[i].isspace():
        fo.write(" "+"\n")
    for j in range(len(ls[i])):
        x = ls[i][j]
        print("1type of x:{}".format(type(x)))   ##########
        if x not in s:
            x = x.upper()
            print("2type of x:{}".format(type(x)))   ##########
        else:
            x = x.lower()
            print("3type of x:{}".format(type(x)))   ##########
        print("1 {}".format(x)) ##########
        if x==ls[i][len([i])-1]: #判断是否遍历至每行的末尾
            fo.write(x + "\n")
        else:
            fo.write(x + " ")

fo.close()

f = open("file2save.py","r")
test = f.readlines()
print(test)
