def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print( 'Leap Year' )
            else:
                print( 'Not leap year')
        else:
            print( 'Leap year' )
    else:
        print( 'Not Leap Year ')

year = int(input("Enter the year to check "))
leap_year(year)
