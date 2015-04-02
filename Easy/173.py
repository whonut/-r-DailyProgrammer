from sys import exit


converters = {'me': {'inches': 39.37,
                        'miles': 0.00062,
                        'attoparsecs': 32.4},
             'mi': {'inches': 63360,
                      'metres': 1609,
                      'attoparsecs': 52155},
             'at': {'inches': 1.21,
                            'miles': 1.9 * (10 ** -5),
                            'metres': 0.0309,},
             'in': {'metres': 0.0254,
                      'miles': 1.58 * (10 ** -5),
                      'attoparsecs': 0.82},
             'ki': {'pounds': 2.2,
                          'ounces': 35.27,
                          'hogsheads of beryllium': 1/440.7},
             'po': {'kilograms': 0.45,
                       'ounces': 16,
                       'hogsheads of beryllium': 1/971.6},
             'ou': {'kilograms': 0.028,
                       'ounces': 1.0/16,
                       'hogsheads of beryllium': 1/(971.6*16)},
             'ho': {'kilograms': 440.7,
                       'ounces': 16*971.6,
                       'hogsheads of beryllium': 971.6}}

while True:
    stmt = raw_input("Enter conversion or type 'exit': ")
    if stmt == 'exit':
        sys.exit()
    parsed = stmt.split(' ')
    old_num = float(parsed[0])
    old_unit = parsed[1]
    new_unit = stmt[stmt.find('to')+3:]
    singulars = {'metres': 'metre',
                 'inches': 'inch',
                 'miles': 'mile',
                 'attoparsecs': 'attoparsec',
                 'kilograms': 'kilogram',
                 'pounds': 'pound',
                'ounces': 'ounce',
                'hogsheads of beryllium': 'hogshead of beryllium'}


    if new_unit in converters[old_unit[:2]].keys():
        new_num = str(old_num * converters[old_unit[:2]][new_unit])
        if new_num == 1:
            new_unit = singulars[new_unit]
            print str(old_num), old_unit, 'is', new_num, new_unit
    else:
         print str(old_num), old_unit, 'cannot be converted into', new_unit
    

        
        


