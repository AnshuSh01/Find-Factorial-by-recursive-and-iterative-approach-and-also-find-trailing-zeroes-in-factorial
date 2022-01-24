def Factorial_Recursive(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*Factorial_Recursive(num-1)

def Factorial_iterative(num):
    fac=1
    
    for i in range(num):
        fac=fac*(i+1)
    return fac   
    
def trailing_zeroes(num):
    no=Factorial_iterative(num)
    count_zeroes=0
    while no%10==0:
        no=no/10
        count_zeroes=count_zeroes+1
    return count_zeroes       
     

if __name__ == '__main__':
    inputNo=int(input("Enter the no. for which u want the Factorial\n"))   
    
    print(f"Factorial of {inputNo}! by recursive approach  is - ",Factorial_Recursive(inputNo))
    print(f"Factorial of {inputNo}! by iterative approach  is - ",Factorial_iterative(inputNo))
     
    print(f"trailing zeroes in {inputNo}! is - ",trailing_zeroes(inputNo))
     