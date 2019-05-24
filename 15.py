#The infinite looping and break

var = 1
while var==1 :
    num = raw_input("Write the number : ")
    print "You entered number : ", num
    #comment below command will make it infinite loop
    if (int(num) == 10) : break
print "Good Bye"     