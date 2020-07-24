import random
import time

chords = []
 
file = open('chords.txt', 'r')
chords = file.read().splitlines()

num_disp = int(input("How many chords do you want? "))
delay = int(input("How long of a delay do you want (secs)? "))

for i in range(num_disp):
    print("------------------")
    print(chords[random.randint(0, len(chords) - 1)])
    print("------------------")
    time.sleep(delay)

print("Chord Session Complete")
file.close()