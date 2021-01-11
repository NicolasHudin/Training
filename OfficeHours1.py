"""
        OFFICE HOURS 1:
            
NO LECTURING, NO NEW INFORMATION
questions, clarification, etc...
not mandatory if you have no questions

"""

#Strings, commands, when and why.

#Reading data and ensuring the proper data type

#When writing a string "" or '' can be useful

#print(""hello"") < Doesn't work

print('"hello"') #prints "hello"

print("'hello'") #prints 'hello' 


"""
Important to distinguish between integers and floats because some
functions later on only take either int or float or str
"""

print(int("1")+1)

print("1"+str(1))


#An application of concepts we've learned in terms of a simple equation

m = float(input("mass value in kg:"))

#input function prints a string and expects a str value back from user
#str value can't be added or multiplied to numbers
#float() function converts it to float so it can be multiplied

c = (299792458)

# setting variable to a constant

E = m * (c**2)

# using known equation e = mc^2

print(E)

#next, list
#