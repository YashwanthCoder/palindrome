original_string = input("enter the desired input =")
original_string = original_string.lower()
reversed_string = ''.join(reversed(original_string))
if reversed_string == original_string:
    print("It is palindromme")
else:
    print("not a palindrome")
