def Solve() -> None:
    languages = ['python', 'perl', 'c']

    for lang in languages:
        if lang in ['python', 'perl']:
            print("%6s need interpretor" % lang)
        elif lang in ['c', 'java']:
            print("%6s need compiler %6s"%(lang, lang))
        else:
            print("should not reach here")


Solve()

