"""
Colorama - работа с цветами
"""
from colorama import init, Fore, Back, Style
init(autoreset=True)                               # AutoRest цвета после каждого print

#=======================================================================================================================
# Fore - цвет текста
print(f'{Fore.BLACK}Fore.BLACK')
print(f'{Fore.LIGHTBLACK_EX}Fore.LIGHTBLACK_EX')
print(f'{Fore.WHITE}Fore.WHITE')
print(f'{Fore.LIGHTWHITE_EX}Fore.LIGHTWHITE_EX')
print(f'{Fore.RED}Fore.RED')
print(f'{Fore.LIGHTRED_EX}Fore.LIGHTRED_EX')
print(f'{Fore.GREEN}Fore.GREEN')
print(f'{Fore.LIGHTGREEN_EX}Fore.LIGHTGREEN_EX')
print(f'{Fore.BLUE}Fore.BLUE')
print(f'{Fore.LIGHTBLUE_EX}Fore.LIGHTBLUE_EX')
print(f'{Fore.CYAN}Fore.CYAN')
print(f'{Fore.LIGHTCYAN_EX}Fore.LIGHTCYAN_EX')
print(f'{Fore.YELLOW}Fore.YELLOW')
print(f'{Fore.LIGHTYELLOW_EX}Fore.LIGHTYELLOW_EX')
print(f'{Fore.MAGENTA}Fore.MAGENTA')
print(f'{Fore.LIGHTMAGENTA_EX}Fore.LIGHTMAGENTA_EX')
print(f'{Fore.RESET}Fore.RESET')                     # Reset цвета текста

# Back - цвет фона
print(f'{Back.BLACK}Back.BLACK')
print(f'{Back.LIGHTBLACK_EX}Back.LIGHTBLACK_EX')
print(f'{Back.WHITE}Back.WHITE')
print(f'{Back.LIGHTWHITE_EX}Back.LIGHTWHITE_EX')
print(f'{Back.RED}Back.RED')
print(f'{Back.LIGHTRED_EX}Back.LIGHTRED_EX')
print(f'{Back.GREEN}Back.GREEN')
print(f'{Back.LIGHTGREEN_EX}Back.LIGHTGREEN_EX')
print(f'{Back.BLUE}Back.BLUE')
print(f'{Back.LIGHTBLUE_EX}Back.LIGHTBLUE_EX')
print(f'{Back.CYAN}Back.CYAN')
print(f'{Back.LIGHTCYAN_EX}Back.LIGHTCYAN_EX')
print(f'{Back.YELLOW}Back.YELLOW')
print(f'{Back.LIGHTYELLOW_EX}Back.LIGHTYELLOW_EX')
print(f'{Back.MAGENTA}Back.MAGENTA')
print(f'{Back.LIGHTMAGENTA_EX}Back.LIGHTMAGENTA_EX')
print(f'{Back.RESET}Back.RESET')                     # Reset цвета фона

# Style - стиль
print(f'{Style.BRIGHT}Style.BRIGHT')                 # Жирный шрифт
print(f'{Style.RESET_ALL}Style.RESET_ALL')           # Reset стиля
#-----------------------------------------------------------------------------------------------------------------------