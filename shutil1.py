import os
import shutil
path = "/Users/hp/Desktop/Class-99/Text.txt"
print("Before moving file:")

print(os.listdir(path))

source = "/Users/hp/Desktop/Class-99/Text.txt"
destination = "/Users/hp/Desktop/Class-99/Text(copy).txt"

dest = shutil.copy(source, destination)
print("After copying files:")
