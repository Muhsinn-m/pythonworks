def poll(age):

    assert age>18,"Invalid age"

    print("voted")

try:
    poll(19)

except Exception as e:
    
    print(e)
