import time

time1= time.strftime("%H:%M:%S")
# print("Time is : ", time1)
if(time1 > "06:00:00" and time1 < "12:00:00" ):
    print("Good Morning !!")
elif(time1 >= "12:00:00" and time1 < "16:00:00"):
    print("Good afternoon !!")
elif(time1 > "16:00:00" and time1 < "20:00:00" ):
    print("Good Evening !!")
else:
    print("Good Night !!")