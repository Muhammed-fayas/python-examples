'''*
   **
   ***
   ****
   *****'''
for value in range(0,6):
    print(value*'*')

def star():
    for value in range(0,6):
        print(value*'*')

star()

def star1(num):
    for value in range(0,num):
        print (value*'*')

star1(7)

class star2:
    def star1(self):
        num=6
        for value in range(0,num):
            print(value*'*')

a=star2()
a.star1()

class star3:
    def __init__(self,num):
        self.num=num

    def star1(self):
            for value in range(0,self.num):
                print(value*'*')

b=star3(6)
b.star1()



list1=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
list1
print(list1)
dir(list1)