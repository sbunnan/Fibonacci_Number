# generate a fibonnaci number by recurssion method and return the sum
def Fibonaci(N,sum):
    if N == 0:
        sum = 0
    elif N == 1:
        sum = 1
    elif N > 1:
        sum = Fibonaci(N-1,sum)+Fibonaci(N-2,sum)
    return sum
    
    
# Check if the sum is prime number
def check_prime(N, sum):
    flag = 0
    if sum > 1:
        for j in range(2, sum / 2, 1):   # condition to check all the possible number divisible by sum, 
            if sum % j == 0:
                flag = 1
        if flag == 1:
            return sum
        else:
            return "BuzzFizz"
    else:
        return sum

# Main function 
def main():
    N =input("Enter the number\n")
    sum = 0
    long(sum)
    sum = Fibonaci(N, sum)
    #print sum
    if sum %3 == 0 and sum % 5 == 0 and sum >2:# check if sum is divisible by both 3 and 5 if yes print "Buzz"  and "Fizz" on seperate line
        return "Buzz\nfizz"
    elif sum % 3 == 0 and sum >2:    # check if sum is divisible by 3 and print "Buzz" if true
        return 'Buzz'
    elif sum % 5 == 0 and sum >5:   # check if sum is divisible ny 5 and print "Fizz" if true
        return 'Fizz'
    else:
        sum = check_prime(N, sum)
    return sum




if __name__ == '__main__':
    a = main()
    print a
