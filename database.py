import sqlite3
import datetime

class DatabaseManager:
    def __init__(self):
        self.db_name = "diary.db"
        self.create_table()

    # データベースファイルに接続する
    def get_connection(self):
        return sqlite3.connect(self.db_name)

    # テーブルが存在しなければ作成する
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS diaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

    # 日記を追加する
    def add_diary(self, content):
        # 日付を取得
        today = datetime.date.today()
        sql = "INSERT INTO diaries (date, content) VALUES (?, ?)"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (today, content))
            conn.commit()
            print(f"DEBUG: Saved {today}, {content}")
    
    # 日記を読み込む
    def get_diaries(self):
        # 新しい順で取得
        sql = "SELECT id date content FROM diaries ORDER BY id DESC"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            
            return cursor.fetchall

if __name__ == "__main__":
    db = DatabaseManager()
    db.add_diary("テスト用データだよー、今日は hello, world! した。")
    print(db.get_diaries)