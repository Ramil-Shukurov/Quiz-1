
WEEKS_IN_MONTH = 4.345

# Define the function "calculate_savings" here.

def main():
  print("Choose an action:")
  print("1.Save more money.")
  print("2.End.")
  choice = int(input())
  while choice != 2:
    print()
    calculate_savings()
    print()
    print("Choose an action:")
    print("1.Save more money.")
    print("2.End.")
    choice = int(input())
  print("\nProgram ends.")

if __name__ == "__main__":
  main()
