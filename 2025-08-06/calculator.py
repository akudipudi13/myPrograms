for i in range(100):
    user_input_str1=input("enter an integer please ")
    user_input_str2=input("enter another integer please ")
    user_input_num1 = int(user_input_str1)
    user_input_num2 = int(user_input_str2)    
    user_input_op = input("please enter an operation ")
    

    if user_input_op == "+":
        print(user_input_num1+user_input_num2)

    elif user_input_op == "-":
        print(user_input_num1-user_input_num2)

    elif user_input_op == "*":
        print(user_input_num1*user_input_num2)

    elif user_input_op == "%":
        print(user_input_num1%user_input_num2)
    else:
        print("please enter correct operation ")


    


    
