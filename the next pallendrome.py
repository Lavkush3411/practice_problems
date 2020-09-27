lis= [12,4,56,668,838,3,769,9,]
lis2=[]
for i in lis:
    if i>10:
        a=i
        while True:
            if str(a)==str(a)[::-1]:
                lis2.append(a)
                break
            a+=1
    else:
        lis2.append(i)
print(lis2)