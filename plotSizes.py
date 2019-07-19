"""
This script allows users to look up the area of a plot,
selected from a list of plots, and specify a unit of area 
measurement to report. 
Plot dimensions must be given in feet.
Area measurements include:
 square kilometers,
 acres,
 hectares,
 square meters,
 square miles,
 square yards,
 square feet,
 and square inches.
When running the script from the command line,
the first agrument is the name of the plot,
and the second is the name of the unit to output.

The script can also be imported as a module, and the function 
calculate_area() can be used on any length, width, and conversion value.
"""

import sys

def make_dicts(area_file, plot_file): #I used generic file names
    """
    Takes a tab separated file of area conversions and a comma separated file
    of plots with lengths and widths and returns two dictionaires.
    
    I used generic variable names for the files in case someday someone
    has a different list of plots or different area units.
    """
    #Here I made dictionaries of the files using dictionary comprehension:
    area_dict = {line.split("\t")[0]: float(line.split("\t")[1].rstrip("\n")) for line in open(area_file, "r")}
    plot_dict = {line.split(",")[0]: [float(line.split(",")[1]),  float(line.split(",")[2].rstrip("\n"))] for line in open(plot_file, "r")}

    #I could also make the dictionaries using loops. They make the same dictionaries as the comprehension above.
    #I have commented out the code below, but you could instead comment out the dictionary comprehension above.
    """
    area_dict = {}
    with open(area_file, "r") as f:
        for line in f:
            line = line.split("\t")
            area_name = line[0]
            area_value = line[1].rstrip("\n") #.rstrip lets me strip the new line character from the right side of each line
            area_value = float(area_value) #the value was a string and needed to be converted to a number
                                       #I chose float instead of integer because there may be decimals
            area_dict[area_name] = area_value

    plot_dict = {}
    with open(plot_file, "r") as f:
        for line in f:
            line = line.split(",")
            plot_name = line[0]
            plot_length = line[1]
            plot_length = float(plot_length)
            plot_width = line[2]
            plot_width = plot_width.rstrip("\n")
            plot_width = float(plot_width)
            plot_value = [plot_length, plot_width] #combine length and width into list
            plot_dict[plot_name] = plot_value
    """
    return area_dict, plot_dict
    
def calculate_area(length, width, convert_num):
    """Takes length, width, and area conversion,
    and returns correct area"""
    area = length * width
    final_area = area / convert_num
    return final_area
    
def main():
    #Make the dictionaries. Enter different filenames if desired:
    area_dict, plot_dict = make_dicts("areas.txt", "plots.txt")
    
    #Error handling for plot names made of up to 4 words:
    n = 1
    plot_name = sys.argv[n]
    for n in range(1,5):
        if plot_name not in plot_dict.keys():
            n += 1
            plot_name = plot_name + " " + sys.argv[n]
        else:
            break
    if plot_name not in plot_dict.keys():
        raise Exception("Plot not found")
            
    #Error handling for area unit made up of two words
    area_unit = sys.argv[-1]
    if area_unit not in area_dict.keys():
        area_unit = sys.argv[-2] + area_unit.capitalize() #capitalize second word if not already done
    if area_unit not in area_dict.keys():
        raise Exception("Area unit not found")
        
    #Look up in dicts and calculate:
    convert_num = area_dict[area_unit]
    dimensions = plot_dict[plot_name]
    final_area = calculate_area(dimensions[0], dimensions[1], convert_num)
    print("{} is {} {}.".format(plot_name, str(final_area), area_unit))
    
if __name__ == "__main__":
    main()
    
    

