# This is just some examples of recursion for future myself (Hello, me!)


# In this explanation function trying to find "Key" in pile of boxes.
# Some boxes can be in other boxes too.
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)  # Recursion
        elif item.is_a_key():
            print('Found the key!')


# In this example just some countdown function
def countdown(num):
    print(num)
    if num <= 1:  # Base case
        return
    else:  # Recursion case
        countdown(num - 1)


# Recursion with stack for factorial calculation (x!)
def factorial(x):
    if x == 1:
        return 1
    else:
        x * factorial(x - 1)
