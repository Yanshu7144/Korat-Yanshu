'''seq = input("Enter the number  =")
element=seq.split(" , ")
list1 = []
for i in range((len(seq) - (len(seq)-1))) :
    list1 . append(element)
print(list1)
a=tuple(list1)
print(a)'''

input_str= input("Enter the number  =")
num_list=[int(num)for num in input_str.split(',')]
num_tuple=tuple(num_list)

print("List of Number =",num_list)
print("tuple of Number =",num_tuple)
