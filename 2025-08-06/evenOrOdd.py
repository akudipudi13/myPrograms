for i in range(10):
    user_input_string=input("enter integer please ")
    user_input_num = int(user_input_string)
    if user_input_num%2 == 0:
        print("your number is even")
    else:
        print("your number is odd")