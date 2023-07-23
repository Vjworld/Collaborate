#Name Validation to be in the specified limits
#of min 3 to max 50 characters long

name = input('Please enter your "Full Name" __')

if len(name) < 3:
    print("Your name must be atleast 3 characters __")
elif len(name) > 50:
    print("Your name can be a maximum of 50 characters __")
else:
    print("Your name looks good as - " + name)
