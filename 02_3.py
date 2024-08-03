def brackets_checker(s: str) -> bool:

    def counter(chr: str, i: int, data: dict):
        if data[chr] != None:
            data[chr] = data[chr] + i
        else:
            data[chr] = i
        return data[chr]

    brackets = {"(": None, "[": None, "{": None}

    for i in range(len(s)):
        chr = s[i]

        if chr == "(":
            brackets["("] = counter(chr, 1, brackets)
        if chr == "[":
            brackets["["] = counter(chr, 1, brackets)
        if chr == "{":
            brackets["{"] = counter(chr, 1, brackets)

        if chr == ")":
            brackets["("] = counter("(", -1, brackets)
        if chr == "]":
            brackets["["] = counter("[", -1, brackets)
        if chr == "}":
            brackets["{"] = counter("{", -1, brackets)

    if brackets["("] != 0 and brackets["["] != 0 and brackets["{"] != 0:
        return "Asymmetrical"
    else:
        return "Symmetrically"


print(brackets_checker("( ) { [ ] ( ) ( ) { } } }"))
print(brackets_checker("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(brackets_checker("( 23 ( 2 - 3)"))
print(brackets_checker("( 11 }"))
