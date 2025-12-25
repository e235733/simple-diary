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

    # テスト用大量追加メソッド
    def add_test_diary(self, count):
        sql = "INSERT INTO diaries (date, content) VALUES (?, ?)"
        test_date0 = datetime.date(2025, 6, 30)

        with self.get_connection() as conn:
            cursor = conn.cursor()
            for i in range(count):
                date = test_date0 - datetime.timedelta(days=count-1-i)
                content = f"{(i+1)**2}円稼げた、明日は{i+1}回腹筋する。"
                print(content)
                cursor.execute(sql, (date, content))
            conn.commit()
        
    
    # 日記リストを読み込む
    def get_list(self):
        # idの小さい順で取得
        sql = "SELECT id, date FROM diaries ORDER BY id DESC"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            
            return cursor.fetchall()
        
    # 内容を読み込む
    def get_content(self, diary_id):
        sql = "SELECT * FROM diaries WHERE id = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (diary_id,))

            return cursor.fetchone()
        
    # 指定されたレコードを削除する
    def delete_diary(self, diary_id):
        sql = "DELETE FROM diaries WHERE id = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (diary_id,))

    # 指定されたレコードを編集する
    def edit_diary(self, diary_id, content):
        sql = "UPDATE diaries SET content = ? WHERE id = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (content, diary_id))

if __name__ == "__main__":
    db = DatabaseManager()
    db.add_test_diary(100)
    print(db.get_list())
    print(db.get_content(25))