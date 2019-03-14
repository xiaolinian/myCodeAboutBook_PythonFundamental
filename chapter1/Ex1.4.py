# chapter1 Ex1.4
# 计算1+2!+3!+4!+...+10!的结果

sum = 0
for i in range(1,11):
    item = 1
    for j in range(1,i+1):
        item = item * j
    sum = sum + item

if __name__ == "__main__":
    print(sum)
