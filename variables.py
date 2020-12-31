import time, calendar
#Enter date in this format -> 19990606
# i.e. Year-month-day
#That is 1999 - Year, 06 - month, 06 - day
dt = input('')
a = (dt[0:4])
b = (dt[4:6])
c = (dt[6:8])
print ('Your Date of Birth is:')
print (c + '-' + b + '-' + a)
x = str(a) + "-" + str(b) + "-" + str(c)
y = time.strftime("%A", time.strptime(x,"%Y-%m-%d"))
print ('The Day was ' + y)
d = calendar.TextCalendar(calendar.SUNDAY)
d.prmonth(int(a), int(b))
