# 9.wap to perform list operations user should enter only list data type,if options
# 1 pop().options 2 sort() options 3 clear() invalid options,invalid data type

user_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
option = int(input("Enter Your Choice 1.pop()  2.sort()  3. clear()"))

if option == 1:
    item_popped = user_list.pop()
    print("Item Popped" , item_popped )
    print("new list",user_list)
elif option == 2:
    print(sorted(user_list))
elif option == 3:
    cleaned_list = user_list.clear()
    print("Cleaned the List!!!")
else:
    print("Invalid Choice")