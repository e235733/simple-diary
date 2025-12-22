import tkinter as tk

class DiaryScreen(tk.Frame):
    def __init__(self, master, db):
        super().__init__(master)
        # 0行目,1列目に対して広がりを許可し、0列目には許可しない
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1) 

        self.make_diary_list(db=db)
        self.make_diary_content()
        self.make_write_operation()

    # リストと追加ボタンのフレームを作成
    def make_diary_list(self, db):
        self.list_operation_frame = tk.Frame(self, bg="black")
        self.list_operation_frame.grid(row=0, column=0, sticky="ns")
        # 1列目に対して広がりを許可し、0列目,0行目に対しては許可しない
        self.list_operation_frame.grid_columnconfigure(0, weight=0, minsize=200)
        self.list_operation_frame.grid_rowconfigure(0, weight=0)
        self.list_operation_frame.grid_rowconfigure(1, weight=1)
        
        # ボタンを作成
        self.add_button_frame = tk.Frame(self.list_operation_frame, bg="red")
        self.add_button_frame.grid(row=0, column=0, sticky="ew")
        self.add_button = tk.Button(self.add_button_frame, text="日記を追加")
        self.add_button.pack(fill="both", expand=True)

        # リストを作成
        self.diary_list_frame = tk.Frame(self.list_operation_frame, bg="blue")
        self.diary_list_frame.grid(row=1, column=0, sticky="nsew")
        self.diary_list = tk.Listbox(self.diary_list_frame, selectmode="browse")
        self.diary_list.pack(fill="both", expand=True)
        # リストに日付を追加していく
        date_list = db.get_list()
        for date in date_list:
            self.diary_list.insert(tk.END, date[1])
        

    # 日記の表示エリアを作成
    def make_diary_content(self):
        self.diary_text_frame = tk.Frame(self, bg="white")
        self.diary_text_frame.grid(row=0, column=1, sticky="nsew")
        self.diary_text = tk.Text(self.diary_text_frame)
        self.diary_text.pack(fill="both", expand=True)
        # テストデータ
        self.diary_text.insert(tk.END, "hello, world!")
        
    def make_show_operation(self):
        # 日記操作フレームを作成
        self.text_operation_frame = tk.Frame(self, bg="gray")
        self.text_operation_frame.place(relx=1, rely=1, anchor="se")
        self.text_operation_frame.propagate(False)
        # 行には広がりを許可せず、列には許可する
        self.text_operation_frame.grid_rowconfigure(0, weight=0)
        self.text_operation_frame.grid_columnconfigure(0, weight=1, minsize=200)
        self.text_operation_frame.grid_columnconfigure(1, weight=1, minsize=200)

        # 編集ボタンフレームを作成
        self.edit_button_frame = tk.Frame(self.text_operation_frame, bg="skyblue")
        self.edit_button_frame.grid(row=0, column=0, sticky="nsew")
        self.edit_button = tk.Button(self.edit_button_frame, text="編集")
        self.edit_button.pack(fill="both")

        # 削除ボタンフレームを作成
        self.delete_button_frame = tk.Frame(self.text_operation_frame, bg="lightblue")
        self.delete_button_frame.grid(row=0, column=1, sticky="nsew")
        self.delete_button = tk.Button(self.delete_button_frame, text="削除")
        self.delete_button.pack(fill="both")

    def make_write_operation(self):
        # 日記操作フレームを作成
        self.text_operation_frame = tk.Frame(self, bg="gray")
        self.text_operation_frame.place(relx=1, rely=1, anchor="se")
        self.text_operation_frame.propagate(False)
        # 行には広がりを許可せず、列には許可する
        self.text_operation_frame.grid_rowconfigure(0, weight=0)
        self.text_operation_frame.grid_columnconfigure(0, weight=1, minsize=200)

        # 決定ボタンフレームを作成
        self.submit_button_frame = tk.Frame(self.text_operation_frame, bg="skyblue")
        self.submit_button_frame.grid(row=0, column=0, sticky="nsew")
        self.submit_button = tk.Button(self.submit_button_frame, text="決定")
        self.submit_button.pack(fill="both")