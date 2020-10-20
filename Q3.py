import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)
  
year = int(input("Enter the year  : "))
month = int(input("Enter the month: "))
print(text_cal.formatmonth(year, month)) 
