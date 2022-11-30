# character=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
# x="".join(character)
# a=x.count('f')
# i=1
# while (i<a):
#     x=x.replace('f',"*",1)
#     i+=1
# res=x.index('f')
# print("the last occurance ",str(res))


character=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
x="".join(character)
a=x.count('c')
i=1
while (i<a):
    x=x.replace('c',"*",1)
    i+=1
res=x.index('c')
print("the last occurance ",str(res))