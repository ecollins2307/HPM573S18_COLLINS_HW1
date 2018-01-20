#HW 1, Problem 4

#create yours list
yours = ["Yale", "MIT", "Berkeley"]

#create mine list
mine = ["ITT Tech", "University of Phoenix", "Cowtown University"]

#combine lists
ours1 = mine + yours

#combine lists method two
ours2 = []
ours2.append(mine)
ours2.append(yours)

#Question 1

#print the lists
print(ours1)
print(ours2)

#Answer: 'ours1' contains a single list which contains the contents of both 'mine' and 'yours'. 'ours2' contains two seperate lists: 'mine' and 'yours'.

#Question 2

#modifing yours
yours.remove("MIT")
yours.insert(1, "OSU")

#print the combined lists again
print(ours1)
print(ours2)

#Answer: As 'ours1' is simply capturing the contents of 'yours' and 'mine' and then creating a new list with said contents, it will not contain the updated 'yours' values. However, as 'ours2' is a list of lists, that is to say to contains the actual 'yours' list, and changes to 'yours' will be reflected in 'ours2'.

