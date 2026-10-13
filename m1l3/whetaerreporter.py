city=input("enter your city name: ")
temp=float(input("enter today's tempture in c: "))
# if temp > 35:
#     print("warning : it is very hot today")
# if temp > 35:
#     print("weather: storching hot")
# elif temp > 25:
#     print("weather: warm and sunny")
# elif temp > 15:
#     print("weather: cool and breezy")
# else:
#     print("weather: cool - stay wram!")
import datetime
import calendar
now = datetime.datetime.now()
print("city", city) 
print("time now", now)
print(calendar. calendar(now.year))