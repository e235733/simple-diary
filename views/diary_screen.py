import tkinter as tk

class DiaryScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # 0行目,1列目に対して広がりを許可し、0列目には許可しない
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.make_diary_list()
        self.make_diary_show()

    # リストと追加ボタンのフレームを作成
    def make_diary_list(self):
        self.list_operation_frame = tk.Frame(self, bg="black")
        self.list_operation_frame.grid(row=0, column=0, sticky="ns")
        # 1列目に対して広がりを許可し、0列目,0行目に対しては許可しない
        self.list_operation_frame.grid_columnconfigure(0, weight=0, minsize=300)
        self.list_operation_frame.grid_rowconfigure(0, weight=0)
        self.list_operation_frame.grid_rowconfigure(1, weight=1)
        
        # ボタンフレームを作成
        self.add_button_frame = tk.Frame(self.list_operation_frame, height=50, bg="red")
        self.add_button_frame.grid(row=0, column=0, sticky="ew")

        #　リストフレームを作成
        self.diary_list_frame = tk.Frame(self.list_operation_frame, bg="blue")
        self.diary_list_frame.grid(row=1, column=0, sticky="nsew")

    # 日記の表示エリアを作成
    def make_diary_show(self):
        self.diary_show_frame = tk.Frame(self, bg="white")
        self.diary_show_frame.grid(row=0, column=1, sticky="nsew")
        # 0行目,0列目に対して広がりを許可し、1行目に対しては許可しない
        self.diary_show_frame.grid_rowconfigure(0, weight=1)
        self.diary_show_frame.grid_columnconfigure(0, weight=1)
        self.diary_show_frame.grid_rowconfigure(1, weight=0)

        # 内容表示フレームを作成
        self.dialy_text_frame = tk.Frame(self.diary_show_frame, bg="pink")
        self.dialy_text_frame.grid(row=0, column=0, sticky="nsew")
        
        # 日記操作フレームを作成
        self.text_operation_frame = tk.Frame(self.diary_show_frame, bg="gray")
        self.text_operation_frame.grid(row=1, column=0, sticky="ew")
        # 全てのグリッドに広がりを許可する
        self.text_operation_frame.grid_rowconfigure(0, weight=1, minsize=50)
        self.text_operation_frame.grid_columnconfigure(0, weight=1)
        self.text_operation_frame.grid_columnconfigure(1, weight=1)

        # 編集ボタンフレームを作成
        self.edit_button_frame = tk.Frame(self.text_operation_frame, bg="skyblue")
        self.edit_button_frame.grid(row=0, column=0, sticky="nsew")

        # 削除ボタンフレームを作成
        self.delete_button_frame = tk.Frame(self.text_operation_frame, bg="lightblue")
        self.delete_button_frame.grid(row=0, column=1, sticky="nsew")