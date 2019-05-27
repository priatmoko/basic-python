# The differences between sys.stdout.write and print

import time, sys
iteration = 555
for k in range(iteration+1) :
    percentage = (float(k) / iteration) * 100
    time_msg = "\r Running process at {0...25%} : "+str(percentage)
    if (percentage>=100) :
        print("\r Process complete                                         ")
    else :        
        print(time_msg)    
    time.sleep(0.001)

