from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror, showinfo
import importlib
import world                                                                   #Модуль с кодом для выполнения комманд кода

class app():
    def __init__():
        ans = ''
        arr = code.split('\n')                                                 #разделение кода построчно
        s = ['from tkinter import *','from tkinter import ttk','from tkinter.ttk import *','class work():', '    def __init__(array, window):', '    pass']  #Базовые строчки кода
        ans = s[0] + '\n' + s[1] + '\n' + s[2] + '\n' + s[3] + '\n'            #начало кода
        for i in range(len(arr)):
            ans += '    ' + arr[i] + '\n'                                      #Записать код с надлежащим отступом
        f = open('world.py', 'w')                                              #Открыть файл для записи
        f.write(ans)                                                           #Запись кода
        f.close()
        try:
            importlib.reload(world)                                            #Перезагрузка библиотеки
            world.work.__init__(array, c)                                      #Выполнение написанного ранее кода
        except Exception  as e:
            showerror(title="Ошибка", message=e)                               #Сообщение об ошибки в коде
    
    def watch_code(self):
        f = open('world.py', 'r')
        a = f.read()
        f.close()
        showinfo(title = 'code', message = a)
    
    def reuse(self):
        a = str(self).split('.!')
        if a[2][:5] == 'label':
            app.create_lbl(self)
        elif a[2][:5] == 'entry':
            app.create_entry(self)
        else:
            app.create_btn(self)
        app.delete_widget(self)
    
    def btn_wid(root, entry1, entry2, entry3):                                 #Получение переменных для создания кнопки
        global name,w,code
        name = entry1.get()
        w = int(entry2.get())
        code = entry3.get("1.0", END)
        root.destroy()
        root.quit()
    
    def create_btn(event):
        root = Tk()
        root.geometry('700x500')
        txt = Label(root,text = 'Введите текст, ширину и напишите код').place(x = 80, y = 5)
        n_entry = Entry(root)
        n_entry.place(x = 5, y = 100)
        w_entry = Entry(root)
        w_entry.place(x = 150, y = 100)
        code_entry = ScrolledText(root, width= 45)
        code_entry.place(x = 300, y = 25)
        code_entry.insert(1.0, 'def __init__(array, window):')
        Button(root, text = 'Выйти', command = lambda root = root: app.btn_wid(root, n_entry, w_entry, code_entry)).place(x = 100, y = 200)
        root.mainloop()
        app.btn_dnd(Button)
        
    def btn_dnd(self):
        global h, cmd, m
        try:
            self.btn = Button(c, text = name, width=int(w), command = app.__init__)
            self.btn.place(x = 70, y = 70)
            self.btn.bind('<B1-Motion>', app.on_drag_motion)
            btns.append(self.btn)
            self.m = Menu(window, tearoff = 0) 
            self.m.add_command(label ="Удалить", command = lambda self = self.btn : app.delete_widget(self))
            self.m.add_command(label = "Переопределить", command = lambda self = self.btn: app.reuse(self))
            self.m.add_command(label = "Просмотреть код", command = lambda self = self.btn : app.watch_code(self))
            self.btn.bind("<Button-3>", lambda event:app.do_popup(self, self.m, event))
        except Exception as e:
            showerror(title = 'Ошибка создания кнопки', message = e)
    
    def create_entry(event):
        root = Tk()
        root.geometry('400x200')
        txt = Label(root,text = 'Введите Название и ширину').place(x = 80, y = 5)
        n_entry = Entry(root)
        n_entry.place(x = 5, y = 100)
        w_entry = Entry(root)
        w_entry.place(x = 200, y = 100)
        Button(root, text="Выйти", command= lambda : app.quit(root, n_entry, w_entry)).place(x = 80, y = 150)
        root.mainloop()
        app.entry_dnd(n_entry)
    
    def entry_dnd(self):
        global entry, w, m
        try:
            self.entry = Entry(c, width = f)
            self.entry.place(x = 30, y = 30)
            self.entry.bind('<B1-Motion>', app.on_drag_motion)
            array.append(self.entry)
            self.m = Menu(window, tearoff = 0) 
            self.m.add_command(label ="Удалить", command = lambda self = self.entry : app.delete_widget(self))
            self.m.add_command(label = "Переопределить", command = lambda self = self.entry:app.reuse(self))
            self.entry.bind("<Button-3>", lambda event:app.do_popup(self, self.m, event))
        except Exception as e:
            showerror(title = 'Ошибка создания поля ввода', message = e)
    
    def create_lbl(event):                                                     #Создание строки на холсте
        root = Tk()                                                            #Окно для создания текстового виджета
        root.geometry('400x200')
        txt = Label(root,text = 'Введите текст и Название строки').place(x = 80, y = 5)
        n_entry = Entry(root)
        n_entry.place(x = 5, y = 100)
        f_entry = Entry(root)
        f_entry.place(x = 200, y = 100)
        Button(root, text="Выйти", command= lambda : app.quit(root, n_entry, f_entry)).place(x = 80, y = 150) #Кнопка для удаления окна
        root.mainloop()
        app.lbl_dnd(f_entry)
    
    def lbl_dnd(self):                                                         #Описание текстового поля
        global lbl, insert, m
        try:
            self.lbl = Label(c, text = n, font = ('Times New Roman', 12), background = 'white')
            self.lbl.place(x = 5, y = 5) 
            self.lbl.bind('<B1-Motion>', app.on_drag_motion)                   #Передвижение виджета
            array.append(self.lbl)
            self.m = Menu(window, tearoff = 0)                                 #Создание меню
            self.m.add_command(label ="Удалить", command = lambda self = self.lbl : app.delete_widget(self))      #добавление команды меню
            self.m.add_command(label = "Переопределить", command = lambda self = self.lbl:app.reuse(self))
            self.lbl.bind("<Button-3>", lambda event:app.do_popup(self, self.m, event)) 
        except Exception as e:
            showerror(title = 'Ошибка создания строки', message = e)           #Бинд на вызов меню
    
    def delete_widget(self):                                                   #Удаление виджета
        self.destroy()
        
    def quit(root, entry1, entry2):                                            #Уничтожение доп. окна
        global n,f
        n = entry1.get()
        f = entry2.get()
        root.destroy()
        root.quit()
    
    def do_popup(self, m, event):                                              #Вызов меню в точе нажатия
        try: 
            m.tk_popup(event.x_root, event.y_root)                             #Вызов меню
        finally: 
            m.grab_release() 
                
    def on_drag_motion(event):                                                 #Перемещение виджета
        widget = event.widget                                                  #Получение виджета
        x = widget.winfo_x() + event.x                                         #Присвоение новой позиции по х
        y = widget.winfo_y() + event.y                                         #Присвоение новой позиции по у
        widget.place(x=x, y=y)                                                 #Установление новой позиции по х и у
    
    def clear_all(array):                                                   #Очистить полотно от виджетов
        global c
        for i in array:
            i.destroy()
        for i in btns:
            i.destroy()
        c.destroy()
        array = []
        c = Canvas(width=500, height=621, bg='white')    
        c.place(x = 149, y = 28)
    
    def main():
        global c, window, k, array, btns
        text = """
            Нажав на любой виджет вне полотна, добавится новый на полотной.
            Нажав и удерживая виджет внутри полотна он будет перемещён.
            При создании виджета когда все данные введены обязательно нажать Enter.
            Важно!!! Все значения полей ввода доступны по обращению к массиву array в порядке их добавления на поле ввода
            В функцию __init__ обязаны поступать переменные array и window
            Подключена библиотека Tkinter
            Также весь код, который будет написан является функцией класса work"""    #Текст - инструкция
        array = []
        btns = []
        k = 0
        window = Tk()   
        window.title('обучалка')
        window.geometry('655x655')
        enter = Entry(text = 'Добавить поле ввода')                            #Добавление ввода
        enter.place(x = 5, y = 30)
        enter.bind('<Button-1>', app.create_entry)                             #Бинд, при нажатие создаётся поле ввода на холсте
        enter.insert(1, 'Добавить поле ввода')                                 #Добавление текста в поле ввода
        button = Button(window, text = 'Добавить кнопку')
        button.place(x = 5, y = 55)
        button.bind('<Button-1>', app.create_btn)                              #Бинд, при нажатие создаётся кнопка на холсте
        label = Label(text = 'Добавить текст', background = 'white')
        label.place(x=5, y =5)
        label.bind('<Button-1>', app.create_lbl)                               #Бинд, при нажатие создаётся текстовое поле на холсте
        c = Canvas(width=500, height=621, bg='white')                          #Создание холста
        c.place(x = 149, y = 28)
        clr_btn = Button(window, width = 23, text = 'Очистить полотно', command = lambda C = c: app.clear_all(array))
        clr_btn.place(x = 0, y = 630)
        msb_btn = Button(window,text = 'Показать инструкцию', width = 83, command = lambda: showinfo(title = 'Инструкция', message = text))
        msb_btn.place(x = 149, y = 0)
        window.configure(bg='gray')                                            #Установление серого заднего фона
        window.mainloop()
        
    
        
app.main()