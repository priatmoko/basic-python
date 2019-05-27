#Dinamic params on method / function using tuple
#pay attention on *, * define the tuple variable


def printinfo(arg1, *vartuple) :
    "This is print variable  passed arguments"
    print" Output is : "
    print arg1
    for var in vartuple :
        print var
    return ;

printinfo("Bismillaah", "nama : Priatmoko", "Contact : 082233459800", "Semangat Kaka")    