name_list=["Ajit yadav", "Arun Kumar" , "Uday Thakur", "Rajiv Gandhi" ," Rabdi Devi"]
name_lis1=[]
for i in name_list:
    j=i.split()
    name_lis1.append(j)
name_lis2=[]
for i_list in name_lis1:
    for j in i_list:
        name_lis2.append(j)
print(name_lis2)
s=set(name_lis2)
name_lis2=list(s)
i=0
name_lis3=[]
while i<len(name_lis2):
    nam=name_lis2[i]+ " "+ name_lis2[i+1]
    name_lis3.append(nam)
    i+=2
print(name_lis3)
