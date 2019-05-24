#Date and Time
import time

ticks = time.time()
print "Number of ticks since 12:00am, january : ", ticks

#getting current time 
localtime = time.localtime(time.time())
print "Local current time : ", localtime

#formatted time
localtime = time.asctime(localtime)
print "Formatted time : ", localtime