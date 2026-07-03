#Import argparse
import argparse
#Description shown when the user asks for help
parser=argparse.ArgumentParser(description="Simple Command-Line Calculator")
#Adding the arguments
parser.add_argument("operation")
parser.add_argument("num1", type = float)
parser.add_argument("num2", type = float)
#Parsing them
args = parser.parse_args()
#Performing the calculations
if args.operation == "add":
    result = args.num1 + args.num2

elif args.operation == "subtract":
    result = args.num2 - args.num1

elif args.operation == "multiply":
    result = args.num2 * args.num1

elif args.operation == "divide":
    if args.num2 == 0:
        print("Cannot divide by zero.")
        exit()
    result = args.num1 / args.num2

else:
    print("Invalid operation")
    exit()
#Displaying the result
print(f"Your result is {result}")

