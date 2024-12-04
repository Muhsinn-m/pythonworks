#find the square of the  entered array

arr={10,20,30,40,2,3}

reslult={}

for num in arr:

    square=num**2

    reslult[num]=square

print(reslult)

#another simple method

result={num:num**3 for num in arr}

print(result)

    