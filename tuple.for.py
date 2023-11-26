names =("ahmed ","amr","ehab","adel","ammar","omar")
for name in names:
    print("hello "+ name)

l1 =("ahmed",77,11.2,True,"hello",False)
for v in l1:
    print(v)
    print(type(v))
    #will print all list
    for v in range(len(l1)):
        print(l1[v])


