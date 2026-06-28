"""
Allure Steps

- Контекст-менеджер <with>  — Для описания НЕСКОЛЬКО шагов в функции
- Декоратор @allure.step()  — Для описания ОДНОГО/ОБЩЕГО шага
— @allure.step() + <with>   — Для описания ОБЩЕГО шага функции + ВНУТРЕННИЕ шаги (sub-steps)
"""
import allure

#=============================================== Контекст-менеджер <with> ==============================================

#-----------------------------------------------------------------------------------------------------------------------
# Test
def test_steps_in_test_with():
    with allure.step('Step-1 in test'):     # Step-1 теста (через <with>)
        ...                                 # ▶ Actions
    with allure.step('Step-2 in test'):     # Step-2 теста (через <with>)
        ...                                 # ▶ Actions

#-----------------------------------------------------------------------------------------------------------------------
# Функции:
def func_1_with():                          # Функция-1
    with allure.step('Step in Func-1'):     # Step функции-1 (через <with>)
        ...                                 # ▶ Actions

def func_2_with():                          # Функция-1
    with allure.step('Step in Func-2'):     # Step функции-2 (через <with>)
        ...                                 # ▶ Actions

#---------------------------
# Test
def test_steps_in_func_with():
    func_1_with()                           # Вызываем функцию-1 (со встроенным step)
    func_2_with()                           # Вызываем функцию-2 (со встроенным step)




#============================================== Декоратор @allure.step() ===============================================
# Функции:
@allure.step('Func-1 (decorator)')          # Step функции-1 (через @decorator)
def func_1_decorator():                     # Функция
    ...                                     # ▶ Actions

@allure.step('Func-2 (decorator)')          # Step функции-2 (через @decorator)
def func_2_decorator():                     # Функция
    ...                                     # ▶ Actions


#--------------------------------
# Test
def test_step_in_func_decorator():
    func_1_decorator()                      # Вызываем функцию-1 (со встроенным step)
    func_2_decorator()                      # Вызываем функцию-2 (со встроенным step)


#=============================================== @allure.step() + with =================================================
# Функция
@allure.step('Build API-Client')                  # ОБЩИЙ step функции (через @декоратор)
def build_api_client():
    with allure.step('Get Auth-token'):           # SUB-step функции (через with)
        ...                                       # ▶ Actions
    with allure.step('Create API client'):        # SUB-step функции (через with)
        ...                                       # ▶ Actions

#------------------------------------------------
# Test
def test_step_in_func_decorator_with_sub_steps():
    build_api_client()                            # Вызываем функцию (c ОБЩИМ step + SUB-steps)



#================================================== Динамические steps =================================================
# Функция
@allure.step('Update to: {last_name}')                     # ДИНАМИЧЕСКИЙ ОБЩИЙ step функции с {Allure-placeholder} <— из параметра функции
def func_decorator_param_with_param(last_name: str):       # Функция (принимает параметр)
    with allure.step(f'Printing Last name: {last_name}'):  # ДИНАМИЧЕСКИЙ SUB-step с f'{string}' <— из параметра функции
        ...                                                # ▶ Actions

#------------------------------------------------------
# Test
@allure.severity(allure.severity_level.NORMAL)
def test_step_in_func_decorator_with_sub_steps_param():
    func_decorator_param_with_param('Connor')              # Вызываем функцию (со встроенными ДИНАМИЧЕСКИМИ steps)
    func_decorator_param_with_param('Smith')               # Вызываем функцию (со встроенными ДИНАМИЧЕСКИМИ steps)
