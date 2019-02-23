#countdownkeyboard input
#positive number should be entered when prompted call countdown

countdown = input("Please enter a positive number only.")
countdown_number = int(countdown)
for num in range(countdown_number, 0, -1):
    print(num,""* num)
print("Blast Off!")


#countup keyboard input
#number entered is negative when prompted call countup

count_up = input("Please enter a negative number only.")
count_up = int(count_up)
for num in range(count_up, 0, 1):
    print(num,""* num)

print("Blast Off!") 



