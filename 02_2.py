from collections import deque


def palindrome_checker(s: str) -> bool:
    s = s.lower().replace(" ", "")
    dque = deque(s)
    while len(dque) > 1:
        if dque.pop() != dque.popleft():
            return False
    return True


print(palindrome_checker("aBBa"))
print(palindrome_checker("aga maga"))
