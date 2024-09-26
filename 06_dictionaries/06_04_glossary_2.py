glossary = {'string': 
            'sequences of characters enclosed within single or double quotes',
            'Boolean Expression':
              'another word for conditional statement',
            'Keys':
              'terms in a dictionary that have values',
            'Python':
              'the program used for coding',
            'Dictionary': 'of set of code that stores values by names'}
for names, definition in glossary.items():
    print(f"{names}, {definition}")
glossary['Value'] = 'what the keys are worth in  dictionary'
glossary['Chain'] = 'used in "if-elif-else" statements'
glossary['Terminal'] = 'the box which displays output of code'
glossary['f-strings'] = 'strings that use variables in them'
glossary['Tuple'] = 'an immutable list'
for names, definition in glossary.items():
    print(f"{names}, {definition}")