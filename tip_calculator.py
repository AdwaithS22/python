print("Welcome to the Tip Calculator.")
contin= input("Press Y to continue \n")

if(contin=="Y" or "y" ):
    total_bill= input("What was the total bill? \n$ ")
    tip_percentage=input("What % tip you want to give?  5 / 7.5 / 10 \n")
    tip=(float(tip_percentage)/100)* float(total_bill)
    print("Tip amount is $ "+ str(tip))
    share_choice=input("Do you want to split your bills? Y/N \n")
    if(share_choice== "Y" or "y"):
        total_members=input("Enter number of people to split within. \n")
        split_share=(float(total_bill)+tip)/float(total_members)
        print("The total expense per person is $" + str(split_share))

#no negative conditions are checked 
#no error handling done