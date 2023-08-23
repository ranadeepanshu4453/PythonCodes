import time
a=time.strftime('%H:%M:%S')
hour=time.strftime('%H')
if(int(hour)<12):
    print("GOOD MORNING")
elif(int(hour)>12):
    print("GOOD AFTERNOON")
    
