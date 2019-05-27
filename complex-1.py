# The differences between sys.stdout.write and print

import time, sys
iteration = 555
for k in range(iteration+1) :
    percentage = (float(k) / iteration) * 100
    time_msg = "\r Running process at {0...25%} : "+str(percentage)
    if (percentage>=100) :
        sys.stdout.write("\r Process complete                                         ")
    else :        
        sys.stdout.write(time_msg)    
    sys.stdout.flush()
    time.sleep(0.001)

