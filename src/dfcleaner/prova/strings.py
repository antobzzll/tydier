

def _rec_slice_str(str1, each):  # used for str_match_ratio sliceeach
    length = len(str1)
    positions = length - 1

    if each > length:
        raise ValueError(f"Invalid each number. Max allowed for provided "
                         f"string is {length}")
    if each < 2:
        raise ValueError(f"Invalid each number. Min allowed is 2")

    start = 0
    end = each
    res = list()
    for _ in range(positions):
        chunk = str1[start:end]
        if len(chunk) == each:
            res.append(chunk)
            start += 1
            end += 1

    return res