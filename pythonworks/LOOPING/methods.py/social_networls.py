users=["arjun","adish","sreerag","adhityan","muhsin","akshay"]

arjun_followers=["adish","sreerag","arjun"]

user_set=set(users)

sujjession=set(users).difference(set(arjun_followers))

print(sujjession)


#find mutual friends

akshay_followers=["adish","adhityan","muhsin"]

set1=set(arjun_followers)

set2=set(akshay_followers)

mutual_friends=set(set1).intersection(set(set2))

print(mutual_friends)