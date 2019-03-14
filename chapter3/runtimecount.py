import time
def runtimecount(problemSize):
    count = 0
    while problemSize > 0:
        problemSize = problemSize // 2
        count = count + 1
    #return count
##if __name__ == "__main__":
##    problemSize = 100000
##    print("problemSize:{},count:{}".format(problemSize,runtimecount(problemSize)))

start = time.time()
runtimecount(10000000)
end = time.time()
print(end-start)
print('hello world')
