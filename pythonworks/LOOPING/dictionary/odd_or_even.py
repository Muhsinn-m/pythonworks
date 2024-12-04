arr=[10,20,30,40,2,3,4,5]

even_squares={num:num**2 for num in arr if num%2==0}

print("even squares=", even_squares)

odd_squares={num:num**2 for num in arr if num%2!=0}

print("odd squares=",odd_squares)


