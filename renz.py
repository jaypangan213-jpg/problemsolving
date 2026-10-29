# Computer Shop Playing System
Rate_per_hour = 15

print("==============================")
print("    ACT-1E COMPUTER SHOP     ")
print("==============================")

name = input("Enter Customer Name: ")

print("\nPlaying Rates:")
print("1. 1 Hour  - ₱15")
print("2. 2 Hours - ₱30")
print("3. 3 Hours - ₱45")
print("4. 4 Hours - ₱60")
print("5. 5 Hours - ₱75")

choice = int(input("\nChoose Playing Time: "))

if choice == 1:
    hours = 1
elif choice == 2:
    hours = 2
elif choice == 3:
    hours = 3
elif choice == 4:
    hours = 4
elif choice == 5:
    hours = 5

else:
    print("Invalid ")
    exit()

total = hours * Rate_per_hour

print("\n==============================")
print("           RECEIPT")
print("==============================")
print("Customer:", name)
print("Playing Time:", hours, "hour(s)")
print("Rate per Hour: ₱", Rate_per_hour)
print("Total: ₱", total)
print("==============================")
print("Enjoy your game!")