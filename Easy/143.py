translation={'O.OO..': 'h', '.OO...': 'i', 'OO....': 'c', 'OOOOO.': 'q', 'O...OO': 'u', 'O.....': 'a', 'O.O.O.': 'l', '.OOO..': 'j', 'O..O..': 'e', 'OO.O..': 'd', 'O..OOO': 'z', 'OO..O.': 'm', 'OO.OO.': 'n', 'OOOO..': 'g', '.OOO.O': 'w', 'O..OO.': 'o', '.OOOO.': 't', 'O.O.OO': 'v', 'OO..OO': 'x', 'OO.OOO': 'y', 'OOO...': 'f', 'O.OOO.': 'r', 'O.O...': 'b', '.OO.O.': 's', 'O...O.': 'k', 'OOO.O.': 'p'}
braille=raw_input('Enter braille: ')
rows=braille.split('\n')
lines=[]
print
text=''
for line in rows:
    lines.append(line.split(' '))

for e in range(0,len(lines[1])):
    text+=translation[lines[0][e]+lines[1][e]+lines[2][e]]
print text
    

