import os

count = 0
for root, dirs, files in os.walk(os.path.curdir):
    for file_str in files:
        if file_str.endswith(".py"):
            count += open(os.path.join(root, file_str), 'rb').read().count(
                    bytes('\n', encoding='utf-8'))

print(f"You wrote {count} lines of code in total.")
