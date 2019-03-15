f = open('novel.txt','rt')
text = f.read()
text = text.lower()
for ch in "~!@#$%^&*()_+-=[]\{}|;':,./<>?":
    text = text.replace(ch," ")
wordlist = text.split()
counts = {}
for word in wordlist:
    counts[word] = counts.get(word,0) + 1

items = list(counts.items())

items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print(word,count)
    
