import time
import random
print( "welcome to standing game")
print()
print( "Everybody stand up ")
print(" Stay standing up util you the has ended")
print("Then sit down")
print("Anyone standing  after time ended is loose")
print( "Anyone sit last before time ended is the winner")
stand_time = random.randint(5,20)
print("Stay standing for " , stand_time, "seconds")
time.sleep(stand_time)
print( "Time is UP")