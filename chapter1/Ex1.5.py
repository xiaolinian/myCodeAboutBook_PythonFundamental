# chapter1 Ex1.5
# 猴子吃桃问题

num = 1
for i in range(4,0,-1):
    num = (num + 1) * 2
    print(i,num)
    

if __name__ == "__main__":
    print(num)
