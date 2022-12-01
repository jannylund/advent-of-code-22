from day01 import *

food = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_day01():
    items = food.splitlines()
    assert len(items) == 14

    groups = get_groups(items)
    group_sums = get_group_sums(groups)
    assert max(group_sums) == 24000

    max_sums = sorted(group_sums, reverse=True)
    assert sum(max_sums[:3]) == 45000
