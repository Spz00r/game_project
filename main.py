import classes
import random
import objects
import time
import colorama
import objects

from objects import image_01
from colorama import init, Fore, Back, Style
from classes import player
from classes import choose
from dialogs import dialog,choose_01
from objects import objects_food
from random import choice
from dialogs import scenario_01, scenario_02

init(convert=True)

#Ввод

print(dialog.player_info)
time.sleep(1.5)

def info_SCP():
	print('**************************',Fore.YELLOW +'  Архив:\n', (Style.RESET_ALL))
	print("Информация об обьекте", Fore.RED + 'SCP-087', (Style.RESET_ALL),':      | "info"')
	print('Условия содержания обьекта      :     | "conditions"')
	print('Архив спуска человека по', Fore.RED + 'SCP-087', (Style.RESET_ALL),':   | "archive"\n')
	print('**************************\n')
	while True:
		
		choice_info = input("Для пропуска/далее напишите команду 'skip'. Ваш выбор: (info, conditions, archive)  ")
		print('\n')
		if choice_info == 'info':
			print(dialog.opisanie_SCP)
			time.sleep(10)
			return info_SCP()
		if choice_info == 'conditions':
			print(dialog.uslovia_SCP)
			time.sleep(10)
			return info_SCP()
		if choice_info == 'archive':
			print(scenario_01())
			time.sleep(3)
			return info_SCP()
		if choice_info == 'skip':
			time.sleep(2)
			scenario_02()
			time.sleep(3)
			choose_01()
			break
		else:
			print('Ошибка ввода. Попробуйте ещё раз.')
info_SCP()


# if choose():
# 	print(dialog.dia)
# else:
# 	print(dialog.dia_02)

# time.sleep(1.5)
# print('Some large text 4...')

# def rand_choice():
# 	while True:
# 		poisk_eda = random.choice(objects_food.food)
# 		print(Fore.YELLOW + 'I\'ll find in bag:', Style.RESET_ALL, poisk_eda)
# 		if poisk_eda == 'Beer':
# 			print('Oh Yess! Found it! That\'s',poisk_eda)
# 			break
# 		else:
# 			time.sleep(2.0)
# 			print('Trying to find beer...')
# 			time.sleep(1)

# rand_choice()

