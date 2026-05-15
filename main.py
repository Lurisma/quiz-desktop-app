import customtkinter as ctk

class App:
   def __init__(self):
      ctk.set_appearance_mode('dark')
      ctk.set_default_color_theme('dark-blue')

      self.window = ctk.CTk()
      self.window.title('QuizApp')
      self.window.geometry('800x600')

      self.main_frame = ctk.CTkFrame(self.window)
      self.login_frame = ctk.CTkFrame(self.window)
      self.register_frame = ctk.CTkFrame(self.window)

      self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.login_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.register_frame.pack(fill='both', expand=True, padx=20, pady=20)

      self.login_frame.pack_forget()
      self.register_frame.pack_forget()

      self.main_label = ctk.CTkLabel(
         self.main_frame,
         text='Викторина',
         font=('Arial', 28)
      )
      self.main_label.pack(pady=50)
      # Кнопки в меню
      self.login_button = ctk.CTkButton(
         self.main_frame,
         text='Вход',
         width=200,
         height=40,
         font=('Arial', 16),
         command=self.show_login
      )
      self.login_button.pack(pady=10)

      self.register_button = ctk.CTkButton(
         self.main_frame,
         text='Регистрация',
         width=200,
         height=40,
         font=('Arial', 16),
         command=self.show_register
      )
      self.register_button.pack(pady=10)
      # Фрейм логина
      self.login_label = ctk.CTkLabel(
         self.login_frame,
         text='Вход',
         font=('Arial', 24)
      )
      self.login_label.pack(pady=30)

      self.login_username_entry = ctk.CTkEntry(
         self.login_frame,
         placeholder_text='Имя пользователя',
         width=250,
         height=40
      )
      self.login_username_entry.pack(pady=10)

      self.login_password_entry = ctk.CTkEntry(
         self.login_frame,
         placeholder_text='Пароль',
         width=250,
         height=40,
         show='*'
      )
      self.login_password_entry.pack(pady=10)

      self.login_submit = ctk.CTkButton(
         self.login_frame,
         text='Войти',
         width=200,
         height=40,
         command=self.do_login
      )
      self.login_submit.pack(pady=20)

      self.back_submit = ctk.CTkButton(
         self.login_frame,
         text='Назад',
         width=200,
         height=40,
         fg_color='gray',
         command=self.show_main
      )
      self.back_submit.pack(pady=20)
      # Фрейм регистрации
      self.register_label = ctk.CTkLabel(
         self.register_frame,
         text='Регистрация',
         font=('Arial', 24)
      )
      self.register_label.pack(pady=30)

      self.register_username_entry = ctk.CTkEntry(
         self.register_frame,
         placeholder_text='Имя пользователя',
         width=250,
         height=40
      )
      self.register_username_entry.pack(pady=10)

      self.register_password_entry = ctk.CTkEntry(
         self.register_frame,
         placeholder_text='Пароль',
         width=250,
         height=40,
         show='*'
      )
      self.register_password_entry.pack(pady=10)

      self.register_submit = ctk.CTkButton(
         self.register_frame,
         text='Зарегистрироваться',
         width=200,
         height=40,
         command=self.do_register
      )
      self.register_submit.pack(pady=20)

      self.back_submit = ctk.CTkButton(
         self.register_frame,
         text='Назад',
         width=200,
         height=40,
         fg_color='gray',
         command=self.show_main
      )
      self.back_submit.pack(pady=20)

      self.window.mainloop()

   def show_main(self):
      self.login_frame.pack_forget()
      self.register_frame.pack_forget()
      self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def show_login(self):
      self.main_frame.pack_forget()
      self.login_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def show_register(self):
      self.main_frame.pack_forget()
      self.register_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def do_login(self):
      print(f'Логин: {self.login_username_entry.get()}, Пароль: {self.login_password_entry.get()}')

   def do_register(self):
      print(f'Логин: {self.register_username_entry.get()}, Пароль: {self.register_password_entry.get()}')

if __name__ == "__main__":
   app = App()