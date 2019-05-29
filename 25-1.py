#raw_input and looping
import sys

def buildFloor(start, end) :
    i = int(start)
    while(i <= end):
        ih=1
        while(ih<= i):
            sys.stdout.write(str(ih))
            ih=ih+1
        print ""
        i=i+start
    return;        

start = raw_input("Enter start number as increment : ")
end = raw_input("Enter end number : ")

buildFloor(int(start), int(end))    