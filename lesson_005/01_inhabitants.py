# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...


from room_1 import folks
import room_2 as r2
print(f' В комнате room_1 живут :')
for name in folks:
    print(name)
for name in r2.folks:
    print(name)
