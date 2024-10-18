import os

       # при помощи метода .getcwd() определим директорию,
       # т.е. текущий рабочий каталог

print('Текущая директория "module_7_5":', os.getcwd())
if os.path.exists('second'):   # метод path.exists указывает путь к  директории ('second')
    os.chdir('second')         # Функция chdir() модуля os изменяет текущий рабочий каталог
else:
    os.mkdir('second')  # Функция mkdir() модуля os создает новый каталог
                       # при этом все родительские каталоги должны уже существовать
    os.chdir('second')
print('Текущая директория:', os.getcwd())
# Функция getcwd() модуля os вернет строку, представляющую текущий рабочий каталог
# os.makedirs(r'third\fourth')          #  r - разделитель
print(os.listdir())
# for i in os.walk('.'):                #  '.' - означает текущую директорию
# Функция walk() модуля os генерирует имена файлов в дереве каталогов
#     print(i)                          #  os.walk - просмотр вложенности в директории
os.chdir(r'E:\PYTHON\Proect_University\module_7\module_7_5')
print('Текущая директория:', os.getcwd())
# print(os.listdir())
# следующие две строки являются генераторами списков 1 - файлов и 2 - директорий
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(f'файлы: {file}')
print(f'директории: {dirs}')
# os.startfile(file[3])  # команда .startfile откроет file[2], где 2 - индекс файла в списке {file}
print(os.stat(file[2]))    # Функция stat()  выведет информацию о файле
print(f'Размер:{os.stat(file[2]).st_size} байт')   # а так  размер файла  в байтах : 2104
# os.system('pip install random2') # а эта комада запустит инсталяцию пакета random2
print("__________________________________________")
path = '.'
rez = sorted(os.listdir(path))  # Функция listdir() модуля os возвращает список из каталога path = '.'
for n, item in enumerate(rez):
    item = os.path.join(path, item)
    print(n+1, item)
print("__________________________________________")
# Функция scandir() модуля os возвращает итератор entry объектов
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

# команда startswith осуществляет поиск name в каталоге ('.')

      # Функция join() модуля os.path правильно соединяет переданный путь path к одному
#  или более компонентов пути *paths.
      # Функция getmtime() модуля os.path возвращает время последней модификации файла
#  или каталога, указанному в path в формате float
      # Функция getsize() модуля os.path возвращает размер файла в байтах (int ),
# указанного в path.
      #  Функция dirname() модуля os.path возвращает имя каталога в пути path.
      # Функция os.path.dirname() может принимать объект, представляющий путь к
#  файловой системе, например такой как pathlib.PurePath.