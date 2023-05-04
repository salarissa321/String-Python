



#--------------------------------
#---------Strings----------
#---------------------------------


myStringOne = ' This Is Single Quote '
myStringTwo = " This Is Double Quotes "

print(myStringOne) #  This Is Single Quote 
print(myStringTwo) #  This Is Double Quotes

myStringThree = " This Is Double Quotes 'Test' "
myStringFour = 'This Is Double Quotes "Test" '  


print(myStringThree) # This Is Double Quotes 'Test' 
print(myStringFour) # This Is Double Quotes "Test"

myStringFive = '''First
Second
Third
'''
myStringSix = """ First
Second
Thrid
"""

print(myStringFive) 
# First 
# Second
# Third
print(myStringSix) 
# First 
# Second
# Third


myStringFive = '''First
Second 'Test' "Test"
Third
'''
myStringSix = """ First
Second "Test" 'Test'
Thrid
"""
print(myStringFive) 
# First 'Test' "Test"
# Second 
# Third
print(myStringSix)
# First 
# Second "Test" 'Test'
# Third