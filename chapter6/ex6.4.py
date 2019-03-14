# ex6.4
f = open("novel.txt","rt")
text = f.read()
f.close()
count = {}
for ch in text:
    if ch != " ":
        count[ch] = count.get(ch,0) + 1
lst = list(count.items())
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    k,v = lst[i]
    print(k,v)
