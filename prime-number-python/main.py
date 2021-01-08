def prime_checker(number):
  is_prime = True 

  for i in range(1, number -1):
    if number % i == 0:
       is_prime = False
  if is_prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")

#ask the user to enter a number and check using the prime checker function

should_continue = True

#create a while loop to keep asking the user to check another number
while should_continue:
  n = int(input("Check this number: "))
  prime_checker(number=n)

  option = input("Would you like to check another number, press 'y' or 'n' to exit").lower()

  if option == "y":
    should_continue
  else: 
    should_continue = False