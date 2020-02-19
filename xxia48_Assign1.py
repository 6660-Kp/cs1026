""""
Name: xinhe xia
ASSIGNMENT 1
"""
name=input("hello ! wellcome to this beverage shop， what is your name ？\n")
if name.isalpha():                                                     # determine if the customer enter a letters
    beverage=input(name+", we provide coffee and tea which do you want?\n") # read in a string
    if beverage.isalpha():                                             # determine if the customer enter letters
        beverage=beverage.lower()                                      # convert the input string to lower case letters
        if beverage=='coffee' or beverage=='c':
            beverage='coffee'                                          #let beverage equal to coffee
            size=input(name+" ok coffee and about the size ?  large , medium or small ? \n")       # read in a string
            if size.isalpha():                                         # determine if the customer enter a letters
                size=size.lower()                                      # convert the input string to lower case letters
                if'medium'==size  or 'm'==size :                       # determine if the input equal to medium or m
                    print(name+" "+size+"ok Medium is gonna be :$2.50 ")
                    Flavoring=input(name+", what kind of flavor do you want add vanilla($0.25),none($0.0) or chocolate($0.75)\n") # read in a string
                    if Flavoring.isalpha() or Flavoring=="" or Flavoring.isspace():                            # determine if the customer enter a letters
                        Flavoring=Flavoring.lower()                    # convert the input string to lower case letters
                        if'none'==Flavoring or Flavoring=="" or Flavoring.isspace():  # determine if the input equal to the condition
                            cost=(2.5)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  medium '+beverage+" no flavoring: is $",cost)        # it will print the cost
                        elif 'vanilla'==Flavoring or 'v'==Flavoring:              # else if input equal to vanilla or v
                            cost=(2.5+0.25)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  medium '+beverage+" vanilla flavoring: is $",cost)   # it will print the cost
                        elif 'chocolate'==Flavoring or 'c'==Flavoring:            # else if input equal to chocolate or c
                            cost=(2.5+0.75)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  medium '+beverage+" chocolate flavoring: is $",cost) # it will print the cost
                        else:
                            print("An Invalid Flavor Error not acceptable")
                    else:
                        print("An Invalid Flavor Error not acceptable")
                elif'large'==size or 'l'==size:
                    print(name+" "+size+"ok Large is gonna be : $3.25 ")
                    Flavoring=input(name+", what kind of flavor do you want add vanilla or chocolate\n")  # read in a string
                    if Flavoring.isalpha()or Flavoring=="" or Flavoring.isspace():                            # determine if the customer enter a letters
                        Flavoring=Flavoring.lower()                    # convert the input string to lower case letters
                        if'none'==Flavoring or Flavoring=="" or Flavoring.isspace():                       # determine if the input equal to the condition
                            cost=(3.5)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  large '+beverage+" no flavoring: is $",cost)         # it will print the cost
                        elif 'vanilla'==Flavoring or 'v'==Flavoring:                                 # else if input vanilla to chocolate or v
                            cost=(3.5+0.25)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  large '+beverage+" vanilla flavoring: is $",cost)
                        elif 'chocolate'==Flavoring or 'c'==Flavoring:                               # else if input equal to chocolate or c
                            cost=(3.5+0.75)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  large '+beverage+" chocolate flavoring: is $",cost)  # it will print the cost
                        else:
                            print("An Invalid Flavor Error not acceptable")
                    else:
                        print("An Invalid Flavor Error not acceptable")
                elif'small'==size or's'==size:
                    print(name+" "+size+"ok small is gonna be : $1.50 ")
                    Flavoring=input(name+", what kind of flavor do you want add vanilla or chocolate\n")  # read in a string
                    if Flavoring.isalpha() or Flavoring=="" or Flavoring.isspace():                            # determine if the customer enter a letters
                        Flavoring=Flavoring.lower()                    # convert the input string to lower case letters
                        if'none'==Flavoring or Flavoring=="" or Flavoring.isspace():
                            cost=(1.5)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  small '+beverage+" no flavoring: is $",cost)
                        elif 'vanilla'==Flavoring or 'v'==Flavoring:
                            cost=(1.5+0.25)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  small '+beverage+" vanilla flavoring: is $",cost)
                        elif 'chocolate'==Flavoring or 'c'==Flavoring:
                            cost=(1.5+0.75)*1.13
                            cost=round(cost, 2)                                                      # round the cost to two decimal
                            print("for "+name+' a  small '+beverage+" chocolate flavoring: is $",cost)
                        else:
                            print("An Invalid Flavor Error not acceptable")
                    else:
                        print("An Invalid Flavor Error not acceptable")
                else:
                    print("An Invalid Size Error not acceptable")
            else:
                print("An Invalid Size Error not acceptable")


        elif beverage=="tea" or beverage=='t':                                                                 # determine if the input equal to the condition
            beverage='tea'                                                                             #let beverage equal to tea
            size=input(name+" ok tea and about the size?  large , medium or small ?\n")
            if size.isalpha():
                size.lower()                                               # convert the input string to lower case letters
                if size=='medium' or size=='m':
                    print(name+" "+size+"ok Medium is gonna be :$2.50 ")
                    Flavoring=input(name+", what kind of flavor do you want add mint($0.5) or lemon($0.25) \n")            # read in a string
                    if Flavoring.isalpha() or Flavoring=="" or Flavoring.isspace():                                # determine if the customer enter a letters
                        Flavoring=Flavoring.lower()                        # convert the input string to lower case letters
                        if'none'==Flavoring or Flavoring=="" or Flavoring.isspace():
                            cost=(2.5)*1.13
                            cost=round(cost, 2)                                                           # round the cost to two decimal
                            print("for "+name+' a  medium '+beverage+" no flavoring: is $",cost)
                        elif 'lemon'==Flavoring or 'l'==Flavoring:
                            cost=(2.5+0.25)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  medium '+beverage+" lemon flavoring: is $",cost)
                        elif 'mint'==Flavoring or 'm'==Flavoring:
                            cost=(2.5+0.5)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  medium '+beverage+" mint flavoring: is $",cost)
                        else:
                            print("An Invalid Flavor Error not acceptable")
                    else:
                        print("An Invalid Flavor Error not acceptable")

                elif 'large'==size or 'l'==size:
                    print(name+" "+size+"ok Large is gonna be : $3.25 ")
                    Flavoring=input(name+", what kind of flavor do you want add lemon or mint \n")
                    if Flavoring.isalpha()or 'n'==Flavoring or''==Flavoring:                                # determine if the customer enter a letters
                        Flavoring=Flavoring.lower()                        # convert the input string to lower case letters
                        if'none'==Flavoring or 'n'==Flavoring or''==Flavoring:
                            cost=(3.5)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  large '+beverage+" no flavoring: is $",cost)
                        elif 'lemon'==Flavoring or 'l'==Flavoring:
                            cost=(3.5+0.25)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  large '+beverage+" lemon flavoring: is $",cost)
                        elif 'mint'==Flavoring or 'm'==Flavoring:
                            cost=(3.5+0.5)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  large '+beverage+" Mint flavoring: is $",cost)
                        else:
                            print("An Invalid Flavor Error not acceptable")
                    else:
                        print("An Invalid Flavor Error not acceptable")
                elif'small'==size or's'==size:
                    print(name+" "+size+"ok small is gonna be : $1.50 ")
                    Flavoring=input(name+", what kind of flavor do you want add mint or lemon \n")
                    if Flavoring.isalpha()or 'n'==Flavoring or''==Flavoring:                                # determine if the customer enter a letters
                        Flavoring=Flavoring.lower()                        # convert the input string to lower case letters
                        if'none'==Flavoring or 'n'==Flavoring or''==Flavoring:
                            cost=(1.5)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  small '+beverage+" no flavoring: is $",cost)
                        elif 'lemon'==Flavoring or 'l'==Flavoring:
                            cost=(1.5+0.25)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  small '+beverage+" lemon flavoring: is $",cost)
                        elif 'mint'==Flavoring or 'm'==Flavoring:
                            cost=(1.5+0.5)*1.13
                            cost=round(cost, 2)
                            print("for "+name+' a  small '+beverage+" Mint flavoring: is $",cost)
                        else:
                            print("An Invalid Flavor Error not acceptable")
                    else:
                        print("An Invalid Flavor Error not acceptable")
                else:
                    print("An Invalid Size Error not acceptable")
            else:
                print("An Invalid Size Error not acceptable")
        else:
            print("An Invalid beverage Error not acceptable")
    else:
        print("An Invalid beverage Error not acceptable")
else:
    print(" An Invalid Name Error not acceptable")
