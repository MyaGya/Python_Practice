def solution(skill, skill_trees):
    skill_trees_sequence = {}

    for i in range(len(skill)):
        skill_trees_sequence[skill[i]] = i

    ans = 0
    for skill_tree in skill_trees:
        sequence = -1
        for i in range(len(skill_tree)):
            if skill_tree[i] not in skill_trees_sequence:
                continue
            if not skill_trees_sequence[skill_tree[i]] == sequence + 1:  # fail
                break
            sequence += 1
        else:
            ans += 1
    return ans


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
