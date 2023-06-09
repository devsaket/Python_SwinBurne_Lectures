# import time

# a = time.time()
# print(a)

# timestamp = total no of seconds from jan 1, 1970 00:00:00 hrs to till now 
#               - also known as epoch time / unix time / machine time

# time.sleep(1)   # execution will be delayed by 1 second
# print(time.ctime(a))    # current date & time 

# Localtime
# print(time.localtime(a))

# localtime in utc format 
# print(time.gmtime(a))

# b = (2019,8,6,10,40,30,1,218,0)
# print(time.mktime(b))
# print(time.asctime(b))

# c= time.localtime(a)
# d = time.strftime("%m-%d-%Y  %H:%M:%S",c)
# print(d)


import datetime 

# current date n time 
# a = datetime.datetime.today()
# print(a)
b = datetime.datetime.now()
print(b)
print(b.year)
print(b.hour)

# c = datetime.datetime(2019,5,3,8,45,30,24)
# print(c)

# date
# print(datetime.date(2019,12,3))
# print(datetime.time(20,12,3))
# print(datetime.date.fromtimestamp(23456789))