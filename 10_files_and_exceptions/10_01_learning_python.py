from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
txt_string = ''
for line in lines:
    txt_string += line

print(txt_string)