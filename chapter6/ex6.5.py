#chapter6 Ex6.5
from random import randint
def chanceCal(times):
    counts = 0
    for i in range(0,times):
        d = []
        for j in range(0,23):
            d.append(randint(0,366))
        if len(set(d)) < len(d):
            counts += 1
    return counts/times
    
if __name__ == "__main__":
    for times in [1000,10000,100000]:
        print("times:{},chance:{}".format(times,chanceCal(times)))
