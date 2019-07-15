"""
This script tells you how many pairs of shoes to buy
for a cow or an octopus.
"""

#import module    #this script does not need any modules


def count_legs(animal):
	if animal == "cow":
		number = 4
	elif animal == "octopus":
		number = 8
	return number
	
def calculate_shoe_order(animal, leg_count):
	pairs = int(leg_count / 2)
	shoe_order = ("For the " 
				 + animal 
				 + ", please order " 
				 + str(pairs)  
				 + " pairs of shoes.")
	return shoe_order
	
def main():
	n = count_legs("octopus")
	final_answer = calculate_shoe_order("octopus", n)
	print(final_answer)
	
	
if __name__ == "__main__":
	main()




