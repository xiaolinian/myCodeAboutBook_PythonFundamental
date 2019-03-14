# ex6.6
import jieba
excludes = {"什么","一个","我们","那里","你们","如今","说道","知道","起来","这里","出来","他们","众人","自己","一面","只见","怎么"}
txt = open ("hongloumeng.txt","r",encoding="utf-8").read()
counts = {}
words = jieba.lcut(txt)
for word in words:
    if len(word) == 1:
        continue
    elif word in excludes:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
lst = list(counts.items())
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(40):
    k,v = lst[i]
    print(k,v)
