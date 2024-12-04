#subtract two numbers either larger or smaller

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,80))