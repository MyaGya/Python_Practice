def solution(n, words):
    history = {}
    prev_last_word = words[0][0]
    for i, word in enumerate(words):
        if word in history:
            break
        if prev_last_word != word[0]:
            break
        history[word] = True
        prev_last_word = word[-1]
    else:
        return [0, 0]

    return [(i % n) + 1, (i // n) + 1]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
