def days_between_dates(day1, month1, year1, day2, month2, year2):
    def year(y):
        if (y%4 == 0 and y%100 != 0) or y%400 ==0:
            return 366
        else:
            return 365

    def month(y, m):
        if year(y) == 366:
            month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month_days = 0
        for i in range(m-1):
            month_days += month_list[i]
        return month_days

    def days_between_years(year1, year2):
        years_days = 0
        for i in range(year1+1, year2):
            if year(i) == 366:
                years_days += 366
            else:
                years_days += 365
        return years_days

    def days_of_year2(y, m, d):
        year2_days = month(y,m) + d
        return year2_days

    def days_of_year1(y, m, d):
        year1_days = year(y) - month(y, m) - d
        return year1_days

    total_days = days_between_years(year1, year2) + days_of_year1(year1, month1, day1) + days_of_year2(year2, month2, day2)
    return total_days
    

print("Enter the initial date in the form of date,month,year")
d1=int(input("Enter the day: "))
m1=int(input("Enter the month: "))
y1=int(input("Enter the year: "))
print("Enter the final date in the form of date,month,year")
d2=int(input("Enter the day: "))
m2=int(input("Enter the month: "))
y2=int(input("Enter the year: "))

if y1<y2:
    print("The elapsed days between the dates ",d1,"-",m1,"-",y1," and ",d2,"-",m2,"-",y2," is ",days_between_dates(d1, m1, y1, d2, m2, y2)," days")
elif y1==y2:
    if m1<m2:
        print("The elapsed days between the dates ",d1,"-",m1,"-",y1," and ",d2,"-",m2,"-",y2," is ",days_between_dates(d1, m1, y1, d2, m2, y2)," days")
    elif m1==m2:
        if d1>d2:
            print("Enter the correct schema of dates")
            exit()
        elif d1==d2:
            print("There are no days elapsed between the given dates")
        else:
            print("The elapsed days between the dates ",d1,"-",m1,"-",y1," and ",d2,"-",m2,"-",y2," is ",days_between_dates(d1, m1, y1, d2, m2, y2)," days")
    else:
        print("Enter the correct schema of dates")
        exit()         
else:
    print("Enter the correct schema of dates")
    exit()
