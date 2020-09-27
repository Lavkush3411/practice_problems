import random

table_of=int(input(" enter the table you want = "))
wrong_term=random.randint(3,9)
wrong_t=random.randint(table_of*wrong_term,table_of*(wrong_term+1))
table_list=[]
for i in range(1,11):
    if i==wrong_term:
        table_list.append(wrong_t)
    else:
        table_list.append(i*table_of)
print(table_list)
r_table_l=[i*table_of for i in range(1,11)]
print(r_table_l)
worng_element=[i for i in table_list if i not in r_table_l]
worng_element_no=[i+1 for i,j in enumerate(table_list) if j not in r_table_l]
if len(worng_element)>0:
    print(f" In rohans table element no {worng_element_no}   [{table_of}]*{worng_element_no}={worng_element} is wrong")
else:
    print("It seems rohans table is right")