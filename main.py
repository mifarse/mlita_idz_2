a = "" # Аккумулятор
s = "" # Строка

class ReadError(Exception):
	def __init__(self, ch, a, s):
		self.ch = ch
		print("Программа прервана! Ошибка чтения символа! Ожидался другой символ вместо", ch)
		print(a+"[ ]"+s[1:]+"\n")

def read(ch):
	global a
	global s
	if (len(s) > 0):
		s = s[1:]
	a+=ch

def S0 (ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			S1(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			S2(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def S1(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saa(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sab(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def S2(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sba(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Saa(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saaa(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbbb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sab(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saba(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sabb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sba(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbaa(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbab(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sbb(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbba(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbbb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Saab(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saba(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sabb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Saba(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbaa(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	else:
		raise ReadError(ch, a, s)

def Sabb(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbba(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbbb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sbaa(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saaa(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saab(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sbab(ch):
	global s
	
	if ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sabb(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sbba(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbaa(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	
	elif ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbab(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Saaa(ch):
	global s
	if ch == "B":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Saab(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

def Sbbb(ch):
	global s
	if ch == "A":
		try: # Попытка выполнить чтение
			read (ch)
		except: # иначе ошибка
			raise ReadError(ch, a, s)

		# Мы пробуем передать автомату следующий символ
		try:
			Sbba(s[0])
		except IndexError: # Неудача чтения обусловлена концом строки.
			print("Успешно! Синтаксический анализатор завершил работу.")
	else:
		raise ReadError(ch, a, s)

print("ИДЗ №2 по МЛиТА. Уруков С.Д. (c) 2016 г.")
print("Условие: Последовательность букв A и B, в которой ни одна комбинация из двух букв не повторяется дважды подряд.")
print()

s = input("Введите последовательность букв (Прим.: ААВВАА):").upper()
# Преобразование на всякий случай, если пользователь введет русские символы
s = s.replace("А", "A")
s = s.replace("В", "B")
a = ""
print("На вход получена последовательность '"+s+"'")

S0(s[0]) # Мы отправляем строку на проверку через автоматы