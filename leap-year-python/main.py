#define a function to check a leap year
def leap_checker(year):
  
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("It's a leap year")
      else:
        print("It's not a leap year")
    else:
      print("Leap year")
  else:
    print("Not a leap year")


should_continue = True 
while should_continue:
  year = int(input("Enter a year:  "))
  leap_checker(year)

  option = input("Check another year? 'y' or 'n'").lower()  
  if option == "y":
    should_continue
  else:
    print("Bye")
    should_continue = False
  