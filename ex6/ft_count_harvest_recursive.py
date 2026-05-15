def helper(n: int, day: int):
    if (day <= n):
        print('Day', day)
        helper(n, day + 1)
    else:
        print('Harvest time!')


def ft_count_harvest_recursive():
    n = int(input('Days until harvest: '))
    day = 1
    helper(n, day)
