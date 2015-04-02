import re


def print_hypbin(n):
    start_oz = re.compile('^10')
    oz = re.compile('10')
    tz = re.compile('20')
    ways = [bin(n)[2:]]

    for s in ways:
        # handle leading '10'
        w = start_oz.sub('2', s)
        if w != s and w not in ways:
            ways.append(w)
        # handle other '01's
        for m in oz.finditer(s):
            w = s[:m.start()] + '02' + s[m.end():]
            if m.start() != 0 and w not in ways:
                ways.append(w)
        # handle '20's
        for m in tz.finditer(s):
            w = s[:m.start()] + '12' + s[m.end():]
            if w not in ways:
                ways.append(w)

    for w in ways:
        print w
