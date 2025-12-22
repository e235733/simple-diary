import tkinter as tk
import config
from views.diary_screen import DiaryScreen
from database import DatabaseManager

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_TITLE)
        self.geometry(config.WINDOW_SIZE)
        
        # 画面サイズのグリッドを1つ作成
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        db = DatabaseManager()

        # メイン画面を表示する
        self.diary_screen = DiaryScreen(master=self, db=db)
        self.diary_screen.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()