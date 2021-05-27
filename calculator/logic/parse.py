from exceptions import *


def my_parse(f):

    s = f.split()

    if len(s) != 3:
        raise InvalidFormatException('invalid format')
    else:
        try:
            float(s[0])
            float(s[2])
        except:
            raise InvalidNumberException('invalid number')
        else:
            if s[1] not in '+-*/':
                raise InvalidOperatorException('invalid operator')
        return s[0], s[1], s[2]

    # else:
    #     float(s[0])
    #     float(s[2])
    # except InvalidNumberException:
    #     raise InvalidNumberException
    #
    #
    # if s[1] not in '+/*-':
    #     raise InvalidOperatorException




