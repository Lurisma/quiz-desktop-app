import customtkinter as ctk
import time
from auth import AuthManager
from database import Database

class App:
   def __init__(self):
      ctk.set_appearance_mode('dark')
      ctk.set_default_color_theme('blue')

      self.window = ctk.CTk()
      self.window.title('QuizApp')
      self.window.geometry('800x600')
      self.window.protocol('WM_DELETE_WINDOW', self.on_closing)

      self.db = Database()
      self.auth = AuthManager(self.db)

      self.main_frame = ctk.CTkFrame(self.window, corner_radius=15)
      self.login_frame = ctk.CTkFrame(self.window, corner_radius=15)
      self.register_frame = ctk.CTkFrame(self.window, corner_radius=15)
      self.menu_frame = ctk.CTkFrame(self.window, corner_radius=15)
      self.game_frame = ctk.CTkFrame(self.window, corner_radius=15)

      self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.login_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.register_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.menu_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.game_frame.pack(fill='both', expand=True, padx=20, pady=20)

      self.login_frame.pack_forget()
      self.register_frame.pack_forget()
      self.menu_frame.pack_forget()
      self.game_frame.pack_forget()
      # Фрейм главный
      self.main_label = ctk.CTkLabel(
         self.main_frame,
         text='✨ ВИКТОРИНА ✨',
         font=('Arial', 36, 'bold'),
         text_color='#f1c40f'
      )
      self.main_label.pack(pady=50)

      self.login_button = ctk.CTkButton(
         self.main_frame,
         text='Вход',
         width=200,
         height=40,
         font=('Arial', 16, 'bold'),
         corner_radius=10,
         fg_color='#4a90e2',
         hover_color='#357abd',
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

      self.back_login_button = ctk.CTkButton(
         self.login_frame,
         text='Назад',
         width=200,
         height=40,
         fg_color='gray',
         command=self.show_main
      )
      self.back_login_button.pack(pady=20)
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

      self.back_register_button = ctk.CTkButton(
         self.register_frame,
         text='Назад',
         width=200,
         height=40,
         fg_color='gray',
         command=self.show_main
      )
      self.back_register_button.pack(pady=20)
      # Фрейм меню игры
      self.welcome_label = ctk.CTkLabel(
         self.menu_frame,
         text='',
         font=('Arial', 24)
      )
      self.welcome_label.pack(pady=30)

      self.play_button = ctk.CTkButton(
         self.menu_frame,
         text='ИГРАТЬ',
         width=250,
         height=50,
         font=('Arial', 20, 'bold'),
         corner_radius=15,
         fg_color='#2ecc71',
         hover_color='#27ae60',
         command=self.start_game
      )
      self.play_button.pack(pady=20)

      self.best_score_label = ctk.CTkLabel(
         self.menu_frame,
         text='Ваш лучший счёт: --',
         font=('Arial', 16)
      )
      self.best_score_label.pack(pady=10)

      self.top5_label = ctk.CTkLabel(
         self.menu_frame,
         text='ТОП-5 ИГРОКОВ',
         font=('Arial', 18, 'bold')
      )
      self.top5_label.pack(pady=(30, 10))

      self.top5_textbox = ctk.CTkTextbox(
         self.menu_frame,
         width=300,
         height=160,
         font=('Arial', 14),
         corner_radius=10,
         fg_color='#1e1e1e',
         text_color='#ecf0f1',
         state='disabled'
      )
      self.top5_textbox.pack(pady=10)

      self.logout_button = ctk.CTkButton(
         self.menu_frame,
         text='Выйти из аккаунта',
         width=150,
         height=35,
         font=('Arial', 14),
         corner_radius=8,
         fg_color='#e74c3c',
         hover_color='#c0392b',
         command=self.logout
      )
      self.logout_button.pack(pady=20)
      # Фрейм игры
      self.question_label = ctk.CTkLabel(
         self.game_frame,
         text='Здесь будет вопрос',
         font=('Arial', 20),
         wraplength=700
      )
      self.question_label.pack(pady=50)

      self.option_buttons = []
      for i in range(4):
         btn = ctk.CTkButton(
            self.game_frame,
            text=f'Вариант {i+1}',
            width=400,
            height=40,
            font=('Arial', 14),
            command=lambda i=i: self.check_answer(i)
         )
         btn.pack(pady=5)
         self.option_buttons.append(btn)

      self.score_label = ctk.CTkLabel(
         self.game_frame,
         text='Счёт: 0',
         font=('Arial', 16)
      )
      self.score_label.pack(pady=20)

      self.timer_label = ctk.CTkLabel(
         self.game_frame,
         text="Время: 0 сек",
         font=('Arial', 16)
      )
      self.timer_label.pack(pady=5)

      self.quit_game_button = ctk.CTkButton(
         self.game_frame,
         text='Выйти в меню',
         width=150,
         height=35,
         fg_color='gray',
         command=self.quit_game
      )
      self.quit_game_button.pack(pady=10)

      self.window.mainloop()

   def on_closing(self):
      self.db.close()
      self.window.destroy()

   def show_main(self):
      self.login_frame.pack_forget()
      self.register_frame.pack_forget()
      self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def show_login(self):
      self.main_frame.pack_forget()
      self.register_frame.pack_forget()
      self.login_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def show_register(self):
      self.main_frame.pack_forget()
      self.register_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def do_login(self):
      username = self.login_username_entry.get()
      password = self.login_password_entry.get()
      user_id = self.auth.login(username, password)
      if user_id:
         self.show_menu(username, user_id)

   def do_register(self):
      username = self.register_username_entry.get()
      password = self.register_password_entry.get()
      if self.auth.register(username, password):
         self.show_login()

   def show_menu(self, username, user_id):
      self.current_user_id = user_id
      self.welcome_label.configure(text=f'Привет, {username}!')

      best = self.db.get_best_score(user_id)
      self.best_score_label.configure(text=f'Ваш лучший счёт: {best}')

      self.update_top5()

      self.login_frame.pack_forget()
      self.register_frame.pack_forget()
      self.menu_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def logout(self):
      self.menu_frame.pack_forget()
      self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

   def start_game(self):
      self.current_score = 0
      self.current_question_index = 0
      self.questions = []
      self.time_elapsed = 0
      self.score_label.configure(text='Счёт: 0')
      self.timer_label.configure(text='Время: 0 сек')

      self.menu_frame.pack_forget()
      self.game_frame.pack(fill='both', expand=True, padx=20, pady=20)

      self.load_questions()
      self.show_question()

   def start_timer(self):
      self.question_start_time = time.time()
      self._schedule_timer_update()

   def _schedule_timer_update(self):
      self.timer_after_id = self.window.after(1000, self.update_timer)

   def update_timer(self):
      if hasattr(self, 'question_start_time'):
         elapsed = int(time.time() - self.question_start_time)
         self.timer_label.configure(text=f'Время вопроса: {elapsed} сек')
         self._schedule_timer_update()

   def stop_timer(self):
      if hasattr(self, 'question_start_time'):
         elapsed = int(time.time() - self.question_start_time)
         self.time_elapsed += elapsed
         delattr(self, 'question_start_time')
         if hasattr(self, 'timer_after_id'):
            self.window.after_cancel(self.timer_after_id)
            delattr(self, 'timer_after_id')

   def quit_game(self):
      self.game_frame.pack_forget()
      self.menu_frame.pack(fill='both', expand=True, padx=20, pady=20)
      self.stop_timer()

   def load_questions(self):
      self.questions = self.db.get_random_questions(10)
      if not self.questions:
         print('В базе нет вопросов!')
         self.quit_game()

   def check_answer(self, selected_index):
      self.stop_timer()
    
      q = self.questions[self.current_question_index]
      if selected_index == q['correct']:
         self.current_score += 100
         self.score_label.configure(text=f'Счёт: {self.current_score}')

      self.current_question_index += 1
      self.show_question()

   def show_question(self):
      if self.current_question_index < len(self.questions):
         q = self.questions[self.current_question_index]
         self.question_label.configure(text=q['question'])
         for i, btn in enumerate(self.option_buttons):
            btn.configure(text=q['options'][i])
         self.start_timer()
      else:
         self.end_game()

   def end_game(self):
      correct_answers = self.current_score // 100
      final_score = correct_answers * 100 - self.time_elapsed * 5
      if final_score < 0:
         final_score = 0

      print(f'Игра окончена!')
      print(f'Правильных ответов: {correct_answers}')
      print(f'Общее время: {self.time_elapsed} сек')
      print(f'Итоговый счёт: {final_score}')

      self.db.save_score(self.current_user_id, final_score)

      best = self.db.get_best_score(self.current_user_id)
      self.best_score_label.configure(text=f'Ваш лучший счёт: {best}')
      self.update_top5()

      self.quit_game()

   def update_top5(self):
      self.top5_textbox.configure(state='normal')
      self.top5_textbox.delete("0.0", "end")
      top5 = self.db.get_top5()
      for i, (username, score) in enumerate(top5, 1):
         self.top5_textbox.insert("end", f"{i}. {username} — {score} очков\n")
      self.top5_textbox.configure(state='disabled')

if __name__ == "__main__":
   app = App()