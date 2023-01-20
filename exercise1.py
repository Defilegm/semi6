# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8




def exp(a,b):    
    if b == 1:
        return a 
    if a == 0:
        return 0
    if b < 0 :
        return  1/(a * exp(a,-b-1))
    if b > 0:
        return a * exp(a,b-1)
    if b == 0:
        return 1


    


expf  = lambda a,b: a if b == 1  else a * expf(a,b-1)  # не работает с b <= 0  и с a == 1 


print(expf(3,5))
print(exp(3,-5))