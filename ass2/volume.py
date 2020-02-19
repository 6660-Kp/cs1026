""""
Name: xinhe xia
ASSIGNMENT 2
"""
import math                 #import a math function
def cube(a):                #create a function name cube with variable a
    va=math.pow(a,3)
    print("The volume of a cube with length ",a," is :",va,"\n")
    return va               #return to va
def ellipsoid(r1,r2,r3):    #create a function name ellipsoid with variable r1,r2,r3
    ve=4/3*(math.pi)*r1*r2*r3
    print("The volume of a ellipsoid with radius1 ",r1,",radius2",r2,",radius3",r3,"is :",ve,"\n")
    return ve               #return to ve
def pyramid(b,h):           #creat a function name pyramid with variable b，h
    vp=1/3*(math.pow(b,2))*h
    print("The volume of a pyramid with base ",b," and height",h," is : ",vp,"\n")
    return vp               #return to vp


