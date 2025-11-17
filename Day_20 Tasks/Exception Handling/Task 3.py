try:
    num = input("Enter the number:")
    if not num.isdigit():
        raise ValueError("if the input is not Integer")
    else:
        print(int(num))
        print("valid integer:",num)
except Exception as e:
    print("Error", e)
