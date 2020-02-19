""""
Name: xinhe xia
ASSIGNMENT 2
"""
import volume                                           #import a math function
ac=[] #create a list name ac
ap=[] #create a list name ap
ae=[] #create a list name ae
gg=1
while gg==1:                                            #while gg is equal to 1 do the thing below
    x=input("hello i am a calculator that only can calculate volume for cube,pyramid,ellipsoid.\n"+"please enter the shape you want to calculate\n")
    while x.isalpha():                                  #while gg is equal to 1 do the thing below
        x=x.lower()                                     #lower the letter
        if x=="c" or x=="cube":                         #determine if the input equal to the condition
            a=float(input("cube length"))               #get a input from user
            ac.append(volume.cube(a))                   #put the result to the list  the calculation already down in volume.py
            ac.sort()                                   #order the list
            x=input("what else shape that you want to calculate?\n")
            continue                                    #continue the function
        elif x=="p" or x=="pyramid" :
            b=float(input("pyramid  length "))
            h=float(input("pyramid  height "))
            ap.append(volume.pyramid(b,h))
            ap.sort()
            x=input("what else shape that you want to calculate?\n")
            continue
        elif x=="ellipsoid" or x=="e" :
            r1=float(input("radius1"))
            r2=float(input("radius2"))
            r3=float(input("radius3"))
            ae.append(volume.ellipsoid(r1,r2,r3))
            ae.sort()
            x=input("what else shape that you want to calculate?\n")
            continue
        elif x=="q" or x=="quit":
            if len(ac)==0 and len(ap)==0 and len(ae)==0:
                print("you have reached the end of your session.\n"+"you did not perform and calculations")
                gg=gg+1
                break                                               #if equal break out of the loop
            elif len(ac)==0 and len(ap)==0:                         #check if ac and ap length are both 0
                    print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                    print("Cube :no shape entered")
                    print("Pyramid :no shape entered")
                    print("Ellipsoid :", end = " ")
                    print(*ae, sep=',')               #print list without []
                    gg=gg+1
                    break
            elif len(ae)==0 and len(ap)==0:
                    print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                    print("Cube :", end = " ")
                    print(*ac, sep=',')
                    print("Pyramid :no shape entered")
                    print("Ellipsoid :no shape entered")
                    gg=gg+1
                    break
            elif len(ac)==0 and len(ae)==0:
                    print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                    print("Cube :no shape entered")
                    print("Pyramid : ", end = " ")
                    print(*ap, sep=',')
                    print("Ellipsoid :no shape entered")
                    gg=gg+1
                    break
            elif len(ac)==0 :
                    print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                    print("Cube :no shape entered")
                    print("Pyramid : ", end = " ")
                    print(*ap, sep=',')
                    print("Ellipsoid :", end = " ")
                    print(*ae, sep=',')
                    gg=gg+1
                    break
            elif len(ae)==0 :
                    print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                    print("Cube : ", end = " ")
                    print(*ac, sep=',')
                    print("Pyramid : ")
                    print(*ap, sep=',')
                    print("Ellipsoid :no shape entered")
                    gg=gg+1
                    break
            elif len(ap)==0 :
                    print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                    print("Cube : ", end = " ")
                    print(*ac, sep=',')
                    print("Pyramid :no shape entered")
                    print("Ellipsoid :", end = " ")
                    print(*ae, sep=',')
                    gg=gg+1
                    break

            else:

                print("you have reached the end of your session.\n"+"the volume calculated for each shapes are:  ")
                print("Cube : ", end = " ")
                print(*ac, sep=',')
                print("Pyramid : ", end = " ")
                print(*ap, sep=',')
                print("Ellipsoid :", end = " ")
                print(*ae, sep=',')
                gg=gg+1
                break




