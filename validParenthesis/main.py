s = "()[]{}"
print(s)


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:  # 1
            stack.append(i)
            print(i)

isValid(s)