from utils.timer import get_time, start_timer


def get_groups(items) -> list:
    groups = []
    group = []
    for item in items:
        if item == "":
            groups.append(group)
            group = []
        else:
            group.append(int(item))
    groups.append(group)
    return groups


def get_group_sums(groups) -> list:
    return [sum(group) for group in groups]


if __name__ == "__main__":
    with open("input/day01.txt") as f:
        items = f.read().splitlines()

    start = start_timer()
    groups = get_groups(items)
    group_sums = get_group_sums(groups)

    print("day 01 part 1: max calories {} in {} ms".format(max(group_sums), get_time(start)))

    start = start_timer()
    max_sums = sorted(group_sums, reverse=True)

    print("day 01 part 2: sum of top 3 calories {} in {} ms".format(sum(max_sums[:3]), get_time(start)))
