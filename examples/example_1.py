import shlex


def parse(inp):
    spl = inp.split(" ")
    args = []
    for i in range(len(spl)):
        if spl[i].startswith('"'):
            sentence = ""
            for word in spl[i:]:
                if word.endswith('"'):
                    sentence += f"{word}"
                    args.append(sentence[1:-1])
                else:
                    sentence += f"{word} "
        else:
            args.append(spl[i])
    return args

# print(parse('single words but "this is a full sentence"'))

print(shlex.split('"single words" but "this is a full sentence"'))