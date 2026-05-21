"""
Pytest parametrize (для Тестов)
@pytest.mark.parametrize(...)
"""
"""
Позволяет запустить одну и ту же функцию (тест) с разными входными данными
@pytest.mark.parametrize('param_name', [value_1, value_2, ...])  - c одним параметром
@pytest.mark.parametrize('param_name_1, param_name_2', [(value_1, value_2), ...])  - c несколькими параметрами
"""
import pytest

#================================================ Manual parametrize ===================================================
def test_1():
    assert 1 > 0  # PASSED

def test_2():
    assert 2 > 0  # PASSED

def test_3():
    assert 3 > 0  # PASSED

def test_loop():
    for n in [1, 2, 3]:  # или range(1, 4)
        assert n > 0  # PASSED (❌Bad practice - если тест упадет на первом <n>, то остальные параметры не будут проверены)

#==================================================== Parametrize ======================================================
# 3-in-1
@pytest.mark.parametrize('number', [1, 2, 3])  # —> number = 1, number = 2, number = 3
def test_1(number: int):           # передаем <number>
    assert number > 0              # подставляет КАЖДЫЙ <number>
                                   # [1] PASSED
                                   # [2] PASSED
                                   # [3] PASSED

#========================================== Parametrize (c двумя параметрами) ==========================================
# 3-in-1
@pytest.mark.parametrize('number, expected', [    # <- 'название параметра 2, название параметра 2'
    (1, 1),         # number = 1, expected = 1
    (2, 4),         # number = 2, expected = 4
    (3, 9)          # number = 3, expected = 9
])
def test_2(number: int, expected: int):    # —>передаем <number> и <expected>
    assert number ** 2 == expected  # подставляет КАЖДЫЙ (<number>, <expected>)
                                    # [1-1] PASSED
                                    # [2-4] PASSED
                                    # [3-9] PASSED

#==================================== Multi Parametrize (Множественная параметризация) =================================
# 12-in-1 (3x4)
@pytest.mark.parametrize('host', [       # каждый параметр <host> будет подставлен 3 раза к Windows, MacOS и Linux
    'https://host_1.com',
    'https://host_2.com',
    'https://host_3.com'
    'https://host_4.com'
])
@pytest.mark.parametrize('os', [         # каждый параметр <OS> будет подставлен 4 раза - к host_1, _2, _3 и _4
    'Windows',
    'MacOS',
    'Linux'
])
def test_multi_param(host: str, os: str):   # <- передаем параметры
    ...                                     # [Windows-https://host_1.com] PASSED
                                            # [Windows-https://host_2.com] PASSED
                                            # [Windows-https://host_3.com] PASSED
                                            # [Windows-https://host_4.com] PASSED
                                            # [MacOS-https://host_1.com] PASSED
                                            # [MacOS-https://host_2.com] PASSED
                                            # [MacOS-https://host_3.com] PASSED
                                            # [MacOS-https://host_4.com] PASSED
                                            # [Linux-https://host_1.com] PASSED
                                            # [Linux-https://host_2.com] PASSED
                                            # [Linux-https://host_3.com] PASSED
                                            # [Linux-https://host_4.com] PASSED
#=======================================================================================================================
