### THIS FILE.py IS ONLY FOR TESTING CODES ###
### def-notlouie ###

import time
import sys

# Function for the loading animation
def loading_animation(duration):
    loading_chars = ['|', '/', '-', '\\']  # Frames of the animation
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for char in loading_chars:
            sys.stdout.write(f'\rLoading........ {char}')  # Print on the same line
            sys.stdout.flush()  # Force the output to update
            time.sleep(0.2)  # Pause for a short duration
    print("\rLoading........ Done!    ")  # Final message after loading completes

# Call the function
loading_animation(5)  # Loading animation for 5 seconds



import time
import sys

# Function for the progress bar animation
def progress_bar(duration, bar_length=50):
    for i in range(bar_length + 1):  
        percent = (i / bar_length) * 100
        bar = '█' * i + '-' * (bar_length - i)  # Filling the progress bar
        sys.stdout.write(f'\rLoading: [{bar}] {percent:.0f}%')  # Print progress
        sys.stdout.flush()  # Update terminal output
        time.sleep(duration / bar_length)  # Adjust speed based on duration
    print("\nLoading Complete!")  # Final message after loading completes

# Call the function
progress_bar(5)  # Progress bar runs for 5 seconds


import time
import sys

def bouncing_ball(duration, width=20):
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for i in range(width):
            sys.stdout.write(f'\r{" " * i}o')  # Move ball right
            sys.stdout.flush()
            time.sleep(0.05)
        for i in range(width, 0, -1):
            sys.stdout.write(f'\r{" " * i}o')  # Move ball left
            sys.stdout.flush()
            time.sleep(0.05)
    print("\nBouncing Ball Done!")

bouncing_ball(5)


import time
import sys

def wave_loading(duration):
    wave_chars = ['~   ', ' ~  ', '  ~ ', '   ~']
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for char in wave_chars:
            sys.stdout.write(f'\rLoading... {char}')  # Prints wave-like animation
            sys.stdout.flush()
            time.sleep(0.2)
    print("\rLoading... Done! ")

wave_loading(5)

import time
import sys

def spinning_dots(duration):
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for char in spinner:
            sys.stdout.write(f'\rLoading {char}')  # Prints spinning dots
            sys.stdout.flush()
            time.sleep(0.1)
    print("\rLoading Complete! ")

spinning_dots(2)


import time
import sys

def dot_loading(duration):
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for dots in ['.', '..', '...', '....', '.....', '......' '.......']:
            sys.stdout.write(f'\rLoading{dots} ')  # Prints dots in a sequence
            sys.stdout.flush()
            time.sleep(0.5)
    print("\rLoading... Done!     ")

dot_loading(5)  # Run for 5 seconds


for j in range(6,1-1):

    for v in range(1,j):
        print(" ",end=" ")
    for q in range(7,j -1):
        print("*",end=" ")
    for q in range(6,j -1):
        print("*",end=" ")
    print(j)

for t in range(1,7):
    
    for p in range(1,5):
        print(" ",end=" ")
    for s in range(1,4):
        print("*",end=" ")
    print() 

import time
import sys

for i in range(5, 0, -1):
    sys.stdout.write(f'\rStarting in {i} seconds...')
    sys.stdout.flush()
    time.sleep(1)
print()
print("\nLet's Go!")


# import time
# import datetime
# import sys

# def real_time_clock():
#     try:
#         while True:
#             # Get current time
#             current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#             # Print time on the same line
#             sys.stdout.write(f'\rCurrent Time: {current_time}')  # Overwrite line
#             sys.stdout.flush()  # Update terminal output

#             time.sleep(1)  # Update every second
#     except KeyboardInterrupt:
#         print("\nClock stopped. Goodbye!")  # Graceful exit

# # Call the function
# real_time_clock()


# print(" louie")