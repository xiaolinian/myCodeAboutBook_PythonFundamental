#chapter6 Ex6.1
"""随机密码生成。编写程序，在26个字母大小写和9个数字组成的列表中随机生成10个8位密码."""
from random import randint
def passwordGen():
    lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I',
           'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9']
    plst = []
    for i in range(0,10):
        password = ""
        for j in range(0,8):
            index = randint(0,61)
            password = "".join([password,lst[index]])
        plst.append(password)
    return plst

print(passwordGen())
            
    
