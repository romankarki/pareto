'''
@lru_cache(None)
def dfs(state):
    if base_case:
        return base_value

    res = INF / 0 / False   # depends on problem

    for choice in choices:
        res = combine(res, cost(choice) + dfs(next_state))

    return res

'''