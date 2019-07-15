"""
Below you will find three pieces of code.
For Examples 1-3, add spaces in where they should go.
For examples 4-6, remove spaces from where they should not go.
Refer to the slides to review PEP 8 rules for spaces.
When you are done, check your work by opening spacePracticeAnswers.py.
"""


#Example 1
a=4
b=a*3
if b/a==3:
	print(a,b,b/a)

#Example 2
A=str(a)
print("Everything is right when "+A+" times 3 divided by "+A+" equals 3.")

#Example 3
suspects=["Mrs. Peacock","Miss Scarlet","Mrs. White","Colonel Mustard","Mr. Green","Professor Plum"]
suspects.sort(reverse=True)
print(suspects)


#Example 4
with open ( "spacePractice.py", "r" ) as f :
	firstLine = f.readline ()
	print ( line_1 )

#Example 5
animals = [ "bear" , "wolf" , "coyote" , "rabbit" , "platypus" , "raccoon dog" , "racoon" ]

#Example 6
omnivores = [ ]
omnivores.append (animals [0])
for animal in animals [5 : 7] :
	omnivores. append(animal)
