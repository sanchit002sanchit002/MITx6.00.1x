'''fibnacci use recursion and use dictionary difference 
'''

def  fib(n) :
    '''fibnacci use  recursion
    '''
    global count_fib_calls
    count_fib_calls += 1
    if n == 1 :
        return 1
    elif n ==2 :
        return 2
    else :
        return (fib(n-1) + fib(n-2))


def  fib_use_dict(n, d) :
    '''fibnacci use  dictionary
    '''
    global count_fib_calls
    count_fib_calls += 1
    if n in d :
        return d[n]
    else :
        new_fib = fib_use_dict(n-1, d) + fib_use_dict(n-2, d)
        d[n] = new_fib
        return new_fib

#test code
fibnumber = 12
count_fib_calls = 0

fib(fibnumber)
print ("use recursion  fib function calls : ", count_fib_calls)

d = {1 : 1, 2 : 2}
count_fib_calls = 0

fib_use_dict(fibnumber, d)
print ("use dictionary fib function calls : ", count_fib_calls)


