######################
# Author: Eric Becerril-Blas
# Main Idea: If you have taken statistics, this is the rule of multiplication
# Run in command line with: python TollRoads.py < input9.txt
# Key things,  Dict, Hash
######################

import sys

# Read through the file input and grab statistics
Stat_vals = []
licence_plates = []
flag = False
for line in sys.stdin:
    print (line)
    line = line.strip()
    if line == "":
        flag = True
    if line and flag == False:
        Stat_vals.append(line)
    if flag == True:
        licence_plates.append(line)

#print(Stat_vals)
first_line = Stat_vals[0].split()

this_dict = {}
for n in range(len(Stat_vals)):
    line = Stat_vals[n].split()
    this_dict.update({line[0]:line[1]})
#print(this_dict)

for plate in licence_plates:
    prob = 1
    #print(plate)
    for element in plate:
        #print(element)
        if element in this_dict.keys():
            prob = prob * float(this_dict.get(element, ""))
        else:
            prob = prob * 1
    print(prob)
