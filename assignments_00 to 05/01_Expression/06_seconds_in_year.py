# calculate the number of seconds in a year

days_per_year: int = 365
hours_per_day: int = 24
min_per_hour: int = 60
sec_per_min: int = 60

def seconds_in_year(days_per_year, hours_per_day, min_per_hour, sec_per_min):
    total_seconds =  days_per_year * hours_per_day * min_per_hour * sec_per_min
    print(f"Seconds in one year {total_seconds} sec") 

if __name__ == '__main__':
    # days = input("enter the number of days")
    seconds_in_year(days_per_year, hours_per_day, min_per_hour, sec_per_min)