number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
# get list's size
n = len(number_list)
# iterate list till i is smaller than n
while i < n:
    # check if number is greater than 50
    if number_list[i] > 50:
        # delete current index from list
        del number_list[i]
        # reduce the list size
        n = n - 1
    else:
        # move to next item
        i = i + 1
print(number_list)

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(number_list) - 1, -1, -1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Reverse mapping
new_dict = {value: key for key, value in ascii_dict.items()}
print(new_dict)



# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

# duplicates = []
# for item, count in collections.Counter(sample_list).items():
#     if count > 1:
#         duplicates.append(item)
# print(duplicates)
