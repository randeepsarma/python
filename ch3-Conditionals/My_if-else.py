import time
"""
str=int(input("Enter time:"))
if(str==1):
    print('Good morning' )
elif(str==2):    
    print('Good Evening' )
elif(str==2):    
    print('Good Afternoon' )
else:    
    print('Good Night' )   
"""
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)