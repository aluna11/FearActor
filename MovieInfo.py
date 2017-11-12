import csv

with open('actors.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    predator_table = {}

    for row in readCSV:
        key = row[0]
        my_list = [row[1], row[2]]
        predator_table[key] = my_list
    # print(predator_table)
# close file Here
csvfile.close()
# Printing predator_table keys and values
# for k in predator_table.keys():
#     print(k)
#     # print("key=", k, "value=", predator_table[k])
#     print(k , predator_table[k])

# Asking user for actor name

print("enter actor name:")
name = raw_input()
if name in predator_table.keys():
    print(predator_table[name])
    if int(predator_table[name][1]) == 1:
        print("PREDATOR")
else:
    print("actor not found")
