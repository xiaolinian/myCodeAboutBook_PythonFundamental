# ex6.2
"""
重复元素判定。编写一个接受列表作为参数，如果一个元素在列表中出现了不止一次，则返回True,
但不要改变原来列表的值。同时编写调用这个函数和测试结果的程序。
"""
def isRepeat(lst):
    s = set(lst)
    if len(s)<len(lst):
        return True
    else:
        return False


def isRepeat2(lst):
    newlst = []
    for x in lst:
        if x in newlst:
            return True
        else:
            newlst.append(x)
    return False

if __name__ == "__main__":
    lst = [[1,2,3,2],['a','a'],['b',1],['a']]
    for i in range(len(lst)):
        if isRepeat2(lst[i]):
            print("{} is repeated".format(lst[i]))
        else:
            print("{} is not repeated".format(lst[i]))

