def preFix(strs):
    strs_2 = strs.copy()
    ref = strs_2[0]
    strs_2.remove(ref)

    prefix = []

    for i, char in enumerate(ref):
        sim = [char]
        for index, name in enumerate(strs_2):
            if ref[0] == name[0]:
                for char_2 in range(len(name)):
                    if char == name[char_2]:
                        sim.append((char, name[char_2]))

        for index, name in enumerate(sim):
            if len(sim) == len(strs):
                if type(name) == str:
                    prefix.append(name)

    stringy = ''.join([x for x in prefix])
    if len(stringy) == 0:
        stringy = '\"\"'
    return stringy


print(preFix(["dog", "racecar", "car"]))
print(preFix(["flower", "flow", "flight"]))
print(preFix(["bri", "brian", "brian"]))
print(preFix(["flower", "flow", "light", "flower", "flow", "light"]))
