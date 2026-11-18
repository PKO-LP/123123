from tkinter import *
# Счётчик задач
count = 0
# Функция для кнопки «Добавить задачу»
def add_task():
    global count
    count = count + 1
    name = entry_name.get()
    days = entry_days.get()
    # ОШИБКА 1: попытка сложить строку с числом count без перевода в str() (вызовет TypeError)
    # status_label["text"] = "Задач добавлено: " + count + " | " + name
    # ИСПРАВЛЕННЫЙ ВАРИАНТ: переводим число в строку через str(count)
    status_label["text"] = "Задач добавлено: " + str(count) + " | " + name + " (" + days + " дн.)"
# Функция для кнопки «Очистить поля»
def clear_fields():
    entry_name.delete(0, END)
    entry_days.delete(0, END)
# Главное окно
root = Tk()
root.title("Планировщик задач")
root.geometry("460x560")
# ОШИБКА 2: файл картинки был не в формате PNG(TclError)
# img = PhotoImage(file="logo.jpg")
# ИСПРАВЛЕННЫЙ ВАРИАНТ: пересохранил картинку через Paint в настоящий PNG в папку проекта
img = PhotoImage(file="logo.png")
img_label = Label(image=img)
img_label.pack()
# Первое поле: название задачи
# ОШИБКА 3: название виджета написано с маленькой буквы (слайды 7-8 презентации)
# label_name = label(text="Название задачи")
# ИСПРАВЛЕННЫЙ ВАРИАНТ: класс Label пишется с заглавной буквы
label_name = Label(text="Название задачи")
label_name.pack()
entry_name = Entry()
entry_name.pack()
# Второе поле: длительность
label_days = Label(text="Длительность (дней)")
label_days.pack()
entry_days = Entry()
entry_days.pack()
# Кнопка «Добавить задачу»
# ОШИБКА 4: переданы скобки в command, из-за чего функция срабатывает сразу при запуске
# btn_add = Button(text="Добавить задачу", command=add_task())
# ИСПРАВЛЕННЫЙ ВАРИАНТ: передаём имя функции без скобок
btn_add = Button(text="Добавить задачу", command=add_task)
btn_add.pack()
# Кнопка «Очистить поля»
btn_clear = Button(text="Очистить поля", command=clear_fields)
btn_clear.pack()
# Нижняя метка-счётчик
status_label = Label(text="Задач добавлено: 0")
# ОШИБКА 5: метод pack() написан с заглавной буквы (слайды 7-8 презентации)
# status_label.Pack()
# ИСПРАВЛЕННЫЙ ВАРИАНТ: все методы pack() пишутся с маленькой буквы
status_label.pack()
# Запуск приложения
root.mainloop()
