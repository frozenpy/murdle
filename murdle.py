#!/usr/bin/env python3
import re
import json
# day 210 - has all three scenarios - use raise, found

blacklist = []
yellowlist = []
greenpatterns = []
yellowpatterns = []
pattern5 = '^[a-z]{5}$'
results = []
results2 = []
results3 = []

with open('letters.txt', 'r') as file:
    letters = json.load(file)


def buildict():
        for number in range(1, 6):
                letter_dict = {}
                letter = input(f'what letter is in position {number}?')
                if letter:
                        code = input('what code g-green, y-yellow, b-black?:')
                else:
                        print('no additional inputs')
                        break
                letter_dict['letter'] = letter
                letter_dict['code'] = code
                letter_dict['position'] = number

                letters[f'dict_{letter}{code}{number}'] = letter_dict

                with open('letters.txt', 'w') as file:
                        json.dump(letters, file)

print(f'letters dictionary: \n {letters} \n')

# print('current valid words:')
# print(results3)
cleardict = input('Input clear to erase the dictionary and start \n'
                  'over or press enter to add another word:')
if cleardict == 'clear':
        print('dictionary cleared, starting over...')
        letters = {}
        print(f'letters dictionary {letters}')
        buildict()
        with open('letters.txt', 'w') as file:
                json.dump(letters, file)
else:
        buildict()

for entry, nested in letters.items():
        code = nested["code"]
        letter = nested['letter']
        position = nested['position']

        if code == 'b':
                blacklist.append(letter)
        elif code == 'y':
                yellowlist.append(letter)
                yellowpatterns.append((position - 1) * '.' + letter + (5 - position) * '.')
        elif code == 'g':
                greenpatterns.append((position - 1)*'.'+letter+(5 - position)*'.')
                # need to add ...g. type logic that moves based on position
# with open("wiki-100k-no-dupes.txt", "r") as wordlist:
# with open("words_alpha.txt", "r") as wordlist:
# with open("google-10000-english-no-swears.txt", "r") as wordlist:
with open("combo-words-no-dupes.txt", "r") as wordlist:
        for line_with_nl in wordlist:
                line = line_with_nl.rstrip()
                if re.match(pattern5, line):
                        if not any(char in line for char in blacklist):
                                if all(char in line for char in yellowlist):
                                        results.append(line)

hits = [v for v in results if all(re.match(pattern, v) for pattern in greenpatterns)]
for h in hits:
        results2.append(h)

hits = [v for v in results2 if not any(re.match(pattern, v) for pattern in yellowpatterns)]
for h in hits:
        results3.append(h)

print(results2)
print(f'\nPOSSIBLE WORDS')
for line in sorted(results3):
        print(line)
print(f'POSSIBLE WORDS\n')
print('pre green', len(results))
print('final results', len(results3))
print('blacklist:', blacklist)
print('yellowlist:', yellowlist)
print('greenpatterns:', greenpatterns)
print('yellowpatterns:', yellowpatterns)


