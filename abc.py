# for i in range(1, 5):
#     print(i)


# a = 1+3+\
#     3+6+\
#     1
    
# print(a)

# lista = [1,2,3,4,5]

# listitr = iter(lista)
# while True:
#     try:
#         print(listitr.__next__())
#     except:
#         break

# class Myclass:
#     __hiden = 0
#     def add(self, increment):
#        self. __hiden+=increment
#        print(self.__hiden)
       
# data = Myclass()
# data.add(1)

# print(data__hiden)
       
       

# def prime(n1,n2):
#         for num in range(n1,n2+1):
#             for i in range(2,num):
        
#                 if (num%i)==0:                                                              
#                    # print("not prime no",num)
#                     break
#             else:
#                 print("prime no",num)
# n1 = int(input("enter the no : "))
# n2 = int(input("enter the no : "))
# prime(n1,n2)
        
        
def primeNo(n):
    count =0
    if n<2:
        return False
    for i in range(2, n):
        if (n%i)==0:
            count = count+1
            
    if (count==0):
        print("prime No: ")
    else:
        print("not prime NO: ")
        
n = int(input("enter the No :"))
primeNo(n)