import sys

# Day 5: Print Queue
R, U = sys.stdin.read().strip().split("\n\n")
R = [[int(x) for x in rule.split("|")] for rule in R.split("\n")]
U = [[int(x) for x in update.split(",")] for update in U.split("\n")]


def is_valid_update(update):
    for r in R:
        if r[0] not in update or r[1] not in update:
            continue
        if update.index(r[0]) > update.index(r[1]):
            return False
    return True


def reorder_update(update):
    while not is_valid_update(update):
        for rule in R:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                update[update.index(rule[0])], update[update.index(rule[1])] = (
                    update[update.index(rule[1])],
                    update[update.index(rule[0])],
                )
    return update


p1 = p2 = 0
for update in U:
    if is_valid_update(update):
        p1 += update[len(update) // 2]
    else:
        p2 += reorder_update(update)[len(update) // 2]

print(p1)
print(p2)
