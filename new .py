# a="my name is tanu"
# b=" "
# c=[]
# for i in a:
#     if i==" ":
#         c.append(b)
#         b=" "
#     else:
#         b=b+i
# if b:
#     c.append(b)
# print(c)


a=[10,12,15,18,20]
l1=[]
l2=[]
b=[]
for i in range(len(a)):
    s=str(a[i])
    for j in range(len(s)):
        if j==0:
            s1=0
            l1.append(s[j])
            for k in range(len(l1)):
                s1=s1+int(l1[k])
        if j!=0:
            s2=0
            l2.append(s[j])
            for s in range(len(l2)):
                s2=s2+int(l2[s])
b.append(s1)
b.append(s2)
print(b)