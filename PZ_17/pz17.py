import tkinter as tk
from tkinter import ttk, messagebox

# Создаем основное окно
root = tk.Tk()
root.title("Регистрационная форма")
root.geometry("400x600")
root.resizable(False, False)

# Заголовок
title_label = tk.Label(root, text="РЕГИСТРАЦИЯ", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Фрейм для формы
form_frame = tk.Frame(root)
form_frame.pack(padx=20, pady=10, fill='x')

# Имя
label_name = tk.Label(form_frame, text="Имя:")
label_name.grid(row=0, column=0, sticky='w', pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column=1, pady=5, sticky='ew')

# Фамилия
label_surname = tk.Label(form_frame, text="Фамилия:")
label_surname.grid(row=1, column=0, sticky='w', pady=5)
entry_surname = tk.Entry(form_frame)
entry_surname.grid(row=1, column=1, pady=5, sticky='ew')

# Электронная почта
label_email = tk.Label(form_frame, text="Email:")
label_email.grid(row=2, column=0, sticky='w', pady=5)
entry_email = tk.Entry(form_frame)
entry_email.grid(row=2, column=1, pady=5, sticky='ew')

# Пароль
label_password = tk.Label(form_frame, text="Пароль:")
label_password.grid(row=3, column=0, sticky='w', pady=5)
entry_password = tk.Entry(form_frame, show="*")
entry_password.grid(row=3, column=1, pady=5, sticky='ew')

# Пол (список)
label_gender = tk.Label(form_frame, text="Пол:")
label_gender.grid(row=4, column=0, sticky='w', pady=5)
gender_var = tk.StringVar()
combo_gender = ttk.Combobox(form_frame, textvariable=gender_var)
combo_gender['values'] = ("Мужчина", "Женщина")
combo_gender.current(0)
combo_gender.grid(row=4, column=1, pady=5, sticky='ew')

# Уровень образования (радио кнопки)
label_education = tk.Label(form_frame, text="Образование:")
label_education.grid(row=5, column=0, sticky='w', pady=5)
education_var = tk.StringVar()
radio_highschool = tk.Radiobutton(form_frame, text="Среднее", variable=education_var, value="Среднее")
radio_bachelor = tk.Radiobutton(form_frame, text="Бакалавр", variable=education_var, value="Бакалавр")
radio_master = tk.Radiobutton(form_frame, text="Магистр", variable=education_var, value="Магистр")
radio_highschool.grid(row=5, column=1, sticky='w')
radio_bachelor.grid(row=6, column=1, sticky='w')
radio_master.grid(row=7, column=1, sticky='w')
education_var.set("Бакалавр")  # по умолчанию

# Согласие (чекбокс)
agree_var = tk.BooleanVar()
checkbox_agree = tk.Checkbutton(root, text="Я согласен с условиями", variable=agree_var)
checkbox_agree.pack(pady=10)

# Фрейм для кнопок
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Обработка кнопки отправки
def submit():
    if not agree_var.get():
        messagebox.showwarning("Предупреждение", "Вы должны согласиться с условиями.")
        return
    # Можно добавить проверки заполнения полей
    data = {
        "Имя": entry_name.get(),
        "Фамилия": entry_surname.get(),
        "Email": entry_email.get(),
        "Пароль": entry_password.get(),
        "Пол": gender_var.get(),
        "Образование": education_var.get(),
        "Согласие": agree_var.get()
    }
    messagebox.showinfo("Успех", "Регистрация прошла успешно!")

def cancel():
    root.destroy()

# Кнопки
btn_submit = tk.Button(button_frame, text="Зарегистрироваться", command=submit)
btn_cancel = tk.Button(button_frame, text="Отмена", command=cancel)

btn_submit.pack(side='left', padx=10)
btn_cancel.pack(side='left', padx=10)

# Запуск главного цикла
root.mainloop()