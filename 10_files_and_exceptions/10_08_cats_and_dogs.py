from pathlib import Path

pathcat = Path('cats.txt')
pathdog = Path('dogs.txt')

try:
    contents = pathcat.read_text()
except FileNotFoundError:
    print("Uh-oh, where it go?")

print(contents)

try:
    contentstwo = pathdog.read_text()
except FileNotFoundError:
    print("Uh-oh, where it go?")

print(contentstwo)