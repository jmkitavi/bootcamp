def find_max_min(nums):
    min_ = None
    max_ = None
    for n in nums:
        if n > max_ or max_ is None:
            max_ = n
        if n < min_ or min_ is None:
            min_ = n
    if min_ == max_:
        return [len(nums)]
    else:
        return [min_, max_]