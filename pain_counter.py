import os

count = 0
for root, dirs, files in os.walk(os.path.curdir):
    for file_str in files:
        if file_str.endswith(u".py"):
            count += open(os.path.join(root, file_str)).read().count('\n')

print(f"You wrote {count} lines of code in total.")
