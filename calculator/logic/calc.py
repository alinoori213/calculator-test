def my_calc(s):

    if s[1] == '+':
        return float(s[0]) + float(s[2])
    elif s[1] == '-':
        return float(s[0]) - float(s[2])
    elif s[1] == '*':
        return float(s[0]) * float(s[2])
    elif s[1] == '/':
        if s[1] == 0:
            raise ZeroDivisionError
        else:
            return float(s[0]) / float(s[2])






