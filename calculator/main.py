import sys
from exceptions import *
import calc
from calc import *
from parse import *


def history(my_str):

    with open('history.txt', 'a+') as f:
        f.write(my_str + '\n')


while True:
    new = input()
    history(new)
    if new == 'exit':
        break
    else:

    # my_parse(new)
    # print(calc.my_calc(new))

        try:
            a = my_parse(new)
            print(calc.my_calc(a))
            history(str(calc.my_calc(a)))

        except InvalidNumberException:
            history('number error')
            print('number error')
        except InvalidOperatorException:
            history('operator error')
            print('operator error')
        except InvalidFormatException:
            history('format error')
            print('format error')
        except ZeroDivisionError:
            history('zero divion')
            print('zero divison')

