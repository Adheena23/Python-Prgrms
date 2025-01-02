input_string = input("enter a string")
reversed_string= input_string[: : -1]
if (input_string == reversed_string):
    print("palindrome")
else:
    print("not palindrome")