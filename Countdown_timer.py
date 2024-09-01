
import time

my_time = int(input("Enter the time in seconds : "))

for x in range(my_time,0,-1):    # We are starting form my_time to 0 in reverse order
                                 # We are converting the user input(seconds) to Hours:minutes:seconds
    seconds = x % 60
    minutes = int(x/60) % 60     # We are using int because some number might return a float value
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")        #02 ensures that if the value is less than 10 (a single digit), it will be displayed with a leading zero.
    time.sleep(1)                # This line makes the program pause for 1 second before continuing to the next iteration of the loop.

print("Time's Up !!! ")



