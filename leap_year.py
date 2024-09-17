def check_leap_year():
    year = int(input("Please enter the year you wanna check\n"))
    if year % 4 == 0:
        print("It's a leap year!")
    elif year % 4 == 1:
        print("It's not a leap year!")

check_leap_year()