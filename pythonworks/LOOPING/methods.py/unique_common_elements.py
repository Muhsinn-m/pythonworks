# to print the same elelements form a set 10,20

st1={10,20,30,40,50}

st2={10,20,60,70,80}

insertion_set=st1.intersection(st2)

print(insertion_set)



#union set is printing all the numbers one time only no re printing

union_set=st1.union(st2)

print(union_set)



#differense is a method opposite of insertion

difference_set=st1.difference(st2)

print(difference_set)



#to remove a number from a set

st1.remove(50)

print(st1)