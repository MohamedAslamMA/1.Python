#Class OOPS
class multifunction():
    def AgeGroup():
        age=int(input("Enter the Age:"))
        if(age<=3):
            print("New Born")
            group="New Born"
        elif(age<=6):
            print("Infant")
            group="Infant"
        elif(age<=12):
            print("Toddler")
            group="Toddler"
        elif(age<=36):
            print("Kids")
            group="Kids"
        else:
            print("Children")
            group="Children"
    def OddNumber():
        num=int(input("Enter the number:"))
        if((num%10)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message="even number"
        return message