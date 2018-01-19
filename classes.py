#class #def
import time
from dialogs import dialog
class player:
	print(dialog.welcome)
	time.sleep(1.6)
	player = input("Введите имя игрока: ")
	while True:
		
		if player == '':
			print("Ошибка ввода. Попробуйте снова...")
		else:
			time.sleep(1.7)
			print("Добро пожаловать,",player,'\n')
			break

def choose():
	while True:

		answer = input('Ваш выбор ("Y"/"N") :  ')
		if answer == 'Y':
			return True
			
		elif answer == 'N':
			return False
			
		else:
			print("Ошибка ввода. Попробуйте снова...")

# def intro_choose():
# 	while True:
# 		enter = input('Your choice: ')
# 		if enter = 
			
	

