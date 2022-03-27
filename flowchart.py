move = input("Does it move? yes/no ")

if move == "yes":
    work1 = input("Should it? (yes/no) ")

    if(work1 == "yes"):
        print("Then no problem. ")
    elif(work == "no"):
        print("Then you need some duct tape ! ")
    else:
        print("Answer my question! You didn't type yes or no. ")
elif move == "no":
    work2 = input("Should it? (yes/no) ")

    if work2 == "yes":
        print("You'll need some WD-40! ")
    elif work2 == "no":
        print("Then no problem. ")
    else:
        print("Answer my question!")
