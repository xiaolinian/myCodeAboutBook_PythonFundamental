# chapter1 Ex1.6
# 健康食谱输出

diet = ["西红柿","花椰菜","黄瓜","牛排","虾仁"]
for i in range(0,5):
    for j in range(0,5):
        if i != j:
            print("{}{}".format(diet[i],diet[j]))
