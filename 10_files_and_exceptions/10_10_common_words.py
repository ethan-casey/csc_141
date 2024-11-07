from pathlib import Path
path = Path('bookguten.txt')

contents = path.read_text()

contents.count('the ')

