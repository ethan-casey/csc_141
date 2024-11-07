from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text().replace('python', 'C++')
print(contents)