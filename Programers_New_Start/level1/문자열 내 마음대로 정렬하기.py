def solution(strings, n):
    """

    :type strings: object
    """
    strings.sort(key=lambda x: (x[n], x))
    return strings
