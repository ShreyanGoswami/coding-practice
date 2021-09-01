def removeKdigits(num: str, k: int) -> str:
    if len(num) == k:
        return "0"
    s = []
    for x in num:
        if len(s) == 0:
            s.append(x)
        else:
            while k > 0 and len(s) > 0:
                topOfStack = s[len(s) - 1]
                if topOfStack > x:
                    s.pop()
                    k -= 1
                else:
                    break
            s.append(x)
    while k != 0:
        s.pop()
        k -= 1
    res = "".join(x for x in s).lstrip("0")
    if len(res) == 0:
        return "0"
    return res


if __name__ == "__main__":
    s = "1432219"
    k = 3
    print(removeKdigits(s, k))
