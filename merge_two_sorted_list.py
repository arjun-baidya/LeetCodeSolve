# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.



list1 = [5,8,3]
list2 = [5,7,3]
# list1.insert(len(list1),list2)
list1.append(list2)
final_list = []
for i in list1:
    if isinstance(i,list):
        final_list.extend(i)
    else:
        final_list.append(i)
final_list.sort()
print(final_list)
