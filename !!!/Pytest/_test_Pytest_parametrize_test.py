"""
Pytest parametrize (для Тестов)
@pytest.mark.parametrize()
"""
"""
Позволяет запустить одну и ту же функцию (тест) с разными входными данными
@pytest.mark.parametrize('param_name', [value_1, value_2, ...])  - c одним параметром
@pytest.mark.parametrize('param_name_1, param_name_2', [(value_1, value_2), ...])  - c несколькими параметрами
"""
import pytest

#================================================ Manual parametrize ===================================================
# Manual
def test_1():
    assert 1 > 0  # PASSED

def test_2():
    assert 2 > 0  # PASSED

def test_3():
    assert 3 > 0  # PASSED

# # 3-in-1 (❌Bad practice)
def test_loop():
    for n in [1, 2, 3]:  # или range(1, 4)
        assert n > 0     # PASSED (❌Bad practice - если тест упадет на первом <n>, то остальные параметры не будут проверены)


#==================================================== Parametrize ======================================================
# 3-in-1
@pytest.mark.parametrize('number', [1, 2, 3])  # number = 1, number = 2, number = 3
def test_1(number: int):            # передаем <number>
    assert number > 0               # подставляет КАЖДЫЙ <number>
                                    # [1] PASSED
                                    # [2] PASSED
                                    # [3] PASSED

#========================================== Parametrize (c двумя параметрами) ==========================================
# 3-in-1
@pytest.mark.parametrize('number, expected', [    # 'параметр_1, параметр_2', [
    (1, 1),         # number = 1, expected = 1
    (2, 4),         # number = 2, expected = 4
    (3, 9)          # number = 3, expected = 9
])
def test_2(number: int, expected: int):    # —> передаем <number> и <expected>
    assert number ** 2 == expected  # подставляет КАЖДЫЙ (<number>, <expected>)
                                    # [1-1] PASSED
                                    # [2-4] PASSED
                                    # [3-9] PASSED

#==================================== Multi Parametrize (Множественная параметризация) =================================
# 12-in-1 (3x4)
@pytest.mark.parametrize('comp', [       # каждый параметр <comp> будет подставлен 3 раза к Windows, MacOS и Linux
    'Computer-1',
    'Computer-2',
    'Computer-3',
    'Computer-4'
])
@pytest.mark.parametrize('os', [         # каждый параметр <os> будет подставлен 4 раза - к computer_1, _2, _3 и _4
    'Windows',
    'MacOS',
    'Linux'
])
def test_multi_param(comp: str, os: str):   # <- передаем параметры
    ...                                     # [Windows-Computer-1] PASSED
                                            # [Windows-Computer-2] PASSED
                                            # [Windows-Computer-3] PASSED
                                            # [Windows-Computer-4] PASSED
                                            # [MacOS-Computer-1] PASSED
                                            # [MacOS-Computer-2] PASSED
                                            # [MacOS-Computer-3] PASSED
                                            # [MacOS-Computer-4] PASSED
                                            # [Linux-Computer-1] PASSED
                                            # [Linux-Computer-2] PASSED
                                            # [Linux-hComputer-3] PASSED
                                            # [Linux-Computer-4] PASSED

#=======================================================================================================================
