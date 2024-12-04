def isleapyear(year):

    if  year%100!=0 or year%4==0 and year%100==0 or year%400==0:

        return True

    else:

        return False

def test_is_leap_year():

    assert isleapyear(2024)==True,"non century year check failed"

    assert isleapyear(2025)==False,"invalid non century check failed"

    assert isleapyear(2000)==True,"century leap year check failed"

    assert isleapyear(1900)==False,"invalid century check failed"

    assert isleapyear(-2029)==False,"invalid year check failed"

try:
    test_is_leap_year()

    print("test case pass")

except Exception as e:

    print("test case failed",e)
