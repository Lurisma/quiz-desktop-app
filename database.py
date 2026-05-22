import sqlite3

class Database:
   def __init__(self, db_name='quiz.db'):
      self.db_name = db_name
      self.conn = None
      self.create_connection()
      self.create_tables()

   def create_connection(self):
      self.conn = sqlite3.connect(self.db_name)

   def create_tables(self):
      cursor = self.conn.cursor()
      cursor.execute('''
         CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
         )
   ''')
      cursor.execute('''
         CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
         )
   ''')
      cursor.execute('''
         CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct INTEGER NOT NULL
         )
   ''')
      self.conn.commit()

   def add_user(self, username, password):
      cursor = self.conn.cursor()
      try:
         cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
         )
         self.conn.commit()
         return True
      except sqlite3.IntegrityError:
         return False

   def get_user(self, username):
      cursor = self.conn.cursor()
      cursor.execute(
         'SELECT id, username, password FROM users WHERE username = ?',
         (username,)
      )
      result = cursor.fetchone()
      return result

   def close(self):
      if self.conn:
         self.conn.close()

   def save_score(self, user_id, score):
      cursor = self.conn.cursor()
      cursor.execute(
         'INSERT INTO scores (user_id, score) VALUES (?, ?)',
         (user_id, score)
      )
      self.conn.commit()

   def get_best_score(self, user_id):
      cursor = self.conn.cursor()
      cursor.execute(
         'SELECT MAX(score) FROM scores WHERE user_id = ?',
         (user_id,)
      )
      result = cursor.fetchone()
      return result[0] if result[0] is not None else 0

   def get_top5(self):
      cursor = self.conn.cursor()
      cursor.execute('''
         SELECT users.username, MAX(scores.score) as best_score
         FROM scores
         JOIN users ON scores.user_id = users.id
         GROUP BY users.id
         ORDER BY best_score DESC
         LIMIT 5
      ''')
      return cursor.fetchall()

   def add_question(self, question, opt1, opt2, opt3, opt4, correct):
      cursor = self.conn.cursor()
      cursor.execute('''
         INSERT INTO questions (question, option1, option2, option3, option4, correct)
         VALUES (?, ?, ?, ?, ?, ?)
         ''', (question, opt1, opt2, opt3, opt4, correct))
      self.conn.commit()

   def get_random_questions(self, limit=10):
      cursor = self.conn.cursor()
      cursor.execute('''
         SELECT * FROM questions ORDER BY RANDOM() LIMIT ?
         ''', (limit,))
      rows = cursor.fetchall()

      questions = []
      for row in rows:
         questions.append({
            'id': row[0],
            'question': row[1],
            'options': [row[2], row[3], row[4], row[5]],
            'correct': row[6]
         })
      return questions