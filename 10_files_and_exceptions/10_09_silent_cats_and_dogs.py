from pathlib import Path

pathcat = Path('cats.txt')
pathdog = Path('dogs.txt')

try:
    contents = pathcat.read_text()
except FileNotFoundError:
    pass

print(contents)

try:
    contentstwo = pathdog.read_text()
except FileNotFoundError:
    pass

print(contentstwo)