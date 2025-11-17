from simple_calculation import add, sub, mul, div
from date_today import today_date

def main():
    try:
        a = float(input("enter the first number :"))
        b = float(input("enter the second number :"))
        print("1.Addition 2.Substraction 3.Multiplication 4.Division")
        choice = int(input("enter the choice you want to perform 1-4: "))

        if choice == 1:
            print("today date :", today_date())
            print("Addition :", add(a, b))
        elif choice == 2:
            print("today date :", today_date())
            print("Substraction :", sub(a, b))
        elif choice == 3:
            print("today date :", today_date())
            print("Multiplication :", mul(a, b))
        elif choice == 4:
            print("today date :", today_date())
            print("Division :", div(a, b))
        else:
            print("Invalid choice .. enter valid choice")

    except ValueError:
        print("Please enter valid integer ")
    except ZeroDivisionError:
        print("divisible by zero")
    else:
        print("Operation performed successfully")
    finally:
        print("Calculation attempt finished")

main()
