f=(11,12,13,14,15)
f
type(f)
for value in f:
    print(value)
list1=[]
list2=[]
x=range(1,101)
for value in x:
    if value%2==0:
        list1.append("odd")
    else:
        list2.append("even")
print(list1)
print(list2)


for value in x:
    if value%3==0:
        print(value)

for value in x:
    if (value%3==0)|(value%5==0):
        print(value)

x=range(1,101)
for value in x:
    if value==50:
       continue
    print(value)

v=range(1,11)
mlt=1
for value in v:
    mlt=mlt*value
print(mlt)

g=[11,22,444,55,98,56,100,54,105]

min=g[0]
for value in g:
    if min<value:
        pass
    else:
        min=value
print(min)

mlt



###



list5=[1,3,2,4,5,6,7,8,9,10,3,6]
list6=[]
for value in list5:
    if list5.count (value)==5:
        list6.append(value)
print(list6)

   

   
list1=[1,3,2,4,5,6,7,8,9,10,3,6]
list2=[]
for value in list1:
    if list1.count (value)==1:
        list2.append(value)
print(list2)

   
   

list3=[1,1,3,3,4,3,1,5,5,6,4,5,8,9,5,7,]
list4=[]
for value in list3:
    if list3.count (value)in[1,2]:
        list4.append(value)
print(set[list4])


   