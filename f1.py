my_lst = eval(input("Enter the list: "))
ind = 0
out_mul = 1
print(type(my_lst))
print("Length of the list is: ", len(my_lst))
for i in my_lst:
    out_mul *= my_lst[ind]
    ind += 1
print("The multiplication of all elements in  the list is: ",out_mul)

