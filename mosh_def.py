def read_input():
    try :
        name = input("Name : ")
        age = int(input("Age : "))
        print(name)
        print(age)
    except :
        print("Invalid input, please write numeric input only!")    

read_input()
