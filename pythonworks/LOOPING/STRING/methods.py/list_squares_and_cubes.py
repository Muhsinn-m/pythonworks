#find the squares of the given numbers from the array

arr=[2,3,4,5,6,7,8]

squares=[num**2 for num in arr]

print(squares)




#convert the array to cubes 

cube=[num**3 for num in arr]

print(cube)



#add +5 all numbers from the given array

add5=[num+5 for num in arr]

print(add5)




#print odd numbers

odd_num=[num for num in arr if num%2!=0]

print(odd_num)




#print number greater than 5

num_gt_5=[num for num in arr if num>5]

print(num_gt_5)




         


