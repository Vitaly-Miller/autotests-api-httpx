"""
Allure tags (через Enum)
"""
"""
Enum - для создания перечислений — наборов именованных констант

- Защита от опечаток — IDE подскажет варианты, опечатка вызовет ошибку
- Читаемость — Status.ACTIVE понятнее, чем 1 или "active"
- Единый источник значений — все допустимые варианты в одном месте
- Автодополнение в PyCharm
"""
from enum import Enum

#=======================================================================================================================
class Status(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'
    CANCELLED = 'cancelled'


# ❌Bad practise
status = 'active'
if status == 'active':      # легко опечататься: "actve", "Activ", "AСTIVE"
   print('👍')

# ✅
status = 'active'
if status == Status.ACTIVE:
    print('👍')



# Обращение:
print(Status.ACTIVE)         # Status.ACTIVE
print(Status.ACTIVE.value)   # active
print(Status.ACTIVE.name)    # ACTIVE

# Итерация:
for s in Status:
    print(s.name, s.value)   # ACTIVE active
                             # INACTIVE inactive
                             # DELETED deleted
                             # CANCELLED cancelled

# List
print(list(Status))          # [<Status.ACTIVE: 'active'>, <Status.INACTIVE: 'inactive'>, <Status.DELETED: 'deleted'>, <Status.CANCELLED: 'cancelled'>]
