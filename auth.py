import hashlib

class AuthManager:
   def __init__(self, db):
      self.db = db

   def _hash_password(self, password):
      return hashlib.sha256(password.encode()).hexdigest()

   def login(self, username, password):
      user = self.db.get_user(username)

      if not user:
         print(f'Пользователь {username} не найден')
         return None

      user_id, db_username, hashed_password = user
      if self._hash_password(password) == hashed_password:
         print(f'Добро пожаловать, {username}!')
         return user_id
      else:
         print('Неверный пароль')
         return None

   def register(self, username, password):
      if not username or not password:
         print('Логин и пароль не могу быть пустыми')
         return False

      hashed = self._hash_password(password)
      success = self.db.add_user(username, hashed)

      if success:
         print(f'Пользователь {username} зарегистрирован')
      else:
         print(f'Пользователь {username} уже существует')

      return success