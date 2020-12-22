#Jump To Python의 예제 및 기초 과정을 따라하면서 파이썬에 숙달해지는 것을 목표로 하는 연습 프로젝트


def Solve() -> None:
    languages = ['naver_AI_BOOSTCAMP', 'perl', 'c']

    for lang in languages:
        if lang in ['naver_AI_BOOSTCAMP', 'perl']:
            print("%6s need interpretor" % lang)
        elif lang in ['c', 'java']:
            print("%6s need compiler %6s"%(lang, lang))
        else:
            print("should not reach here")


Solve()

