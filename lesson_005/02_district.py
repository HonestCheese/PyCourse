# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room2 as ch1r2
import district.central_street.house1.room1 as ch1r1
import district.central_street.house2.room1 as ch2r1
import district.central_street.house2.room2 as ch2r2

import district.soviet_street.house1.room1 as sh1r1
import district.soviet_street.house1.room2 as sh1r2
import district.soviet_street.house2.room1 as sh2r1
import district.soviet_street.house2.room2 as sh2r2


modules = [sh1r1, sh1r2, sh2r1, sh2r2, ch1r1, ch2r2, ch1r2, ch2r1]

folks = [folk for module in modules for folk in module.folks]
print('На районе живут', ', '.join(folks))






