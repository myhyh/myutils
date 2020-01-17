# lst中按key_func定义的key聚合成list
def group_by(lst, key_func):
    result = {}
    for item in lst:
        key = key_func(item)
        result.setdefault(key, [])
        result[key].append(item)
    return result
