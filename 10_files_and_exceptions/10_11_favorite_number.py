from pathlib import Path
import json

number = input("What's your favorite number? ")

path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

reading = path.read_text()
yournumber = json.loads(reading)

print(yournumber)