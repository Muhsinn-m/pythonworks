weight=int(input("enter weight in kg:"))

height=int(input("enter height in cm:"))

age=int(input("enter age:"))


gender=input("enter the gender").lower()


print(weight,height,age,gender)


if gender=="male":
    bmr=10*weight + 6.25*height - 5*age+5

elif gender=="female":
    bmr=10*weight+6.25*height-5*age-161
    
else:
    print("""*****please enter valid gender*****""")

print(bmr)

activity_level=int(input("""
             select activity level
            press 1 for sedentery
            press 2 for lightly active
            press 3 for modretly active
            press 4 for very active
            press 5 for extra active"""))
if activity_level==1:
    calorie=bmr*1.2

elif activity_level==2:
    calorie=bmr*1.375

elif activity_level==3:
    calorie=bmr*1.55

elif activity_level==4:
    calarie=bmr*1.725

elif activity_level==5:
    calorie=bmr*1.9

else:
    print("select valid level for activety level*****")

print(f"total number of calories you need in order to maintain your current weight={calorie}")



target_weight=int(input("enter weight to reduse in kg"))

duration=int(input("enter duration in week"))

# 1kg=>7700

calorie_defict=target_weight*7700

days=duration*7

daily_calorie_defict=calorie_defict/days

print(f"daily calorie defict={daily_calorie_defict}")
      
























                        