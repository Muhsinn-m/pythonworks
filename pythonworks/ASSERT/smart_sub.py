def swap_dec(fn):

    def wrapper(num1,num2):

        if num1<num2:

            (num1,num2)=(num2,num1)
    return wrapper


@swap_dec
def smart_sub (num1,num2):

    return num1-num2

@swap_dec
def smart_div (num1,num2):

    return num1/num2

print(smart_sub(10,2))

print(smart_sub(2,10))
 