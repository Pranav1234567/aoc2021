def score(str):
    points = dict()
    points[']'] = 2
    points[')'] = 1
    points['}'] = 3
    points['>'] = 4
    score = 0
    for c in str:
        score *= 5
        score += points[c]
    return score

with open('day10_input.txt') as f:
    lines = f.readlines()
    d = dict()
    d[']'] = '['
    d[')'] = '('
    d['}'] = '{'
    d['>'] = '<'
    reverse_d = dict()
    reverse_d['['] = ']'
    reverse_d['('] = ')'
    reverse_d['{'] = '}'
    reverse_d['<'] = '>'
    points = dict()
    points[']'] = 57
    points[')'] = 3
    points['}'] = 1197
    points['>'] = 25137
    total = 0
    all_scores = []
    for line in lines:
        stack = []
        for c in line.rstrip():
            if stack:
                if c in d and d[c] == stack[-1]:
                    stack = stack[:-1]
                else:
                    stack.append(c)
            else:
                stack.append(c)
        has_illegal_char = False
        for e in stack:
            if e in points:
                has_illegal_char = True
                total += points[e]
                break
        if not has_illegal_char:
            stack_completion = ""
            for e in stack[::-1]:
                stack_completion += reverse_d[e]
            all_scores.append(score(stack_completion))

    all_scores = sorted(all_scores)
    print(all_scores[len(all_scores) // 2])
    print(total)
