import tkinter as tk
from database import DatabaseManager

class DiaryScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.db = DatabaseManager()

        # 0行目,1列目に対して広がりを許可し、0列目には許可しない
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1) 

        self.make_diary_list()
        self.make_diary_content()

    # リストと追加ボタンのフレームを作成
    def make_diary_list(self):
        self.list_operation_frame = tk.Frame(self, bg="black")
        self.list_operation_frame.grid(row=0, column=0, sticky="ns")
        # 1列目に対して広がりを許可し、0列目,0行目に対しては許可しない
        self.list_operation_frame.grid_columnconfigure(0, weight=0, minsize=200)
        self.list_operation_frame.grid_rowconfigure(0, weight=0)
        self.list_operation_frame.grid_rowconfigure(1, weight=1)
        
        # ボタンを作成
        self.add_button_frame = tk.Frame(self.list_operation_frame, bg="red")
        self.add_button_frame.grid(row=0, column=0, sticky="ew")
        self.add_button = tk.Button(self.add_button_frame, text="日記を追加", command=self.on_click_add_button)
        self.add_button.pack(fill="both", expand=True)

        # リストを作成
        self.diary_list_frame = tk.Frame(self.list_operation_frame, bg="blue")
        self.diary_list_frame.grid(row=1, column=0, sticky="nsew")
        self.diary_list = tk.Listbox(self.diary_list_frame, selectmode="browse", exportselection=False)
        self.diary_list.pack(fill="both", expand=True)
        # 選択イベントを紐付ける
        self.diary_list.bind("<<ListboxSelect>>", self.on_diary_select)
        # リストに日付を追加していく
        self.date_list = self.db.get_list()
        for date in self.date_list:
            self.diary_list.insert(tk.END, date[1])

    # 日記の表示エリアを作成
    def make_diary_content(self):
        self.diary_text_frame = tk.Frame(self, bg="white")
        self.diary_text_frame.grid(row=0, column=1, sticky="nsew")
        self.diary_text = tk.Text(self.diary_text_frame)
        self.diary_text.pack(fill="both", expand=True)
        self.diary_text.config(state="disabled")

        # 日記操作フレームを作成
        self.operation_container = tk.Frame(self.diary_text_frame, bg="gray")
        self.operation_container.place(relx=1, rely=1, anchor="se")

        # 閲覧モードのフレームを作成
        self.view_operation_frame = tk.Frame(self.operation_container, bg="gray")
        self.view_operation_frame.grid(row=0, column=0, sticky="nsew")
        # 列には広がりを許可する
        self.view_operation_frame.grid_columnconfigure(0, weight=1, minsize=200)
        self.view_operation_frame.grid_columnconfigure(1, weight=1, minsize=200)
        # 編集、削除ボタンを作成
        self.edit_button = tk.Button(self.view_operation_frame, text="編集")
        self.delete_button = tk.Button(self.view_operation_frame, text="削除", command=self.on_click_delete_button)
        self.edit_button.grid(row=0, column=0, sticky="ew")
        self.delete_button.grid(row=0, column=1, sticky="ew")

        # 入力モードのフレームを作成
        self.input_operation_frame = tk.Frame(self.operation_container, bg="gray")
        self.input_operation_frame.grid(row=0, column=0, sticky="nsew")
        # 列には広がりを許可する
        self.input_operation_frame.grid_columnconfigure(0, weight=1, minsize=200)
        # 保存ボタンを作成
        self.save_button = tk.Button(self.input_operation_frame, text="保存", command=self.on_click_save_button)
        self.save_button.grid(row=0, column=0, sticky="ew")

        # 最初はどのボタンも非表示にしておく
        self.view_operation_frame.grid_remove()
        self.input_operation_frame.grid_remove()

    # リストの要素が選択された場合の処理
    def on_diary_select(self, event=None):
        selection = self.diary_list.curselection()
        # イベントがなければ終了
        if not selection:
            return
        
        # 日記の内容を取得
        index = selection[0]
        diary_id = self.date_list[index][0]
        detail_data = self.db.get_content(diary_id=diary_id)
        content = detail_data[2]
        
        # 表示
        self.diary_text.config(state="normal")
        self.diary_text.delete("1.0", tk.END)
        self.diary_text.insert(tk.END, content)
        self.diary_text.config(state="disabled")
        # 閲覧モードへ変更
        self.show_view_operation()

    # 追加ボタンが押された場合の処理
    def on_click_add_button(self):
        # リストの選択を解除
        self.diary_list.select_clear(0, tk.END)
        # テキストを削除
        self.diary_text.config(state="normal")
        self.diary_text.delete("1.0", tk.END)
        # 書き込みモードへ変更
        self.show_input_operation()

    # 保存ボタンが押された場合の処理
    def on_click_save_button(self):
        # ユーザの入力内容を取得
        input_content = self.diary_text.get("1.0", tk.END)
        # データベースに保存
        self.db.add_diary(input_content)
        # リストの内容をリロード
        self.reload_diary_list()
        # 閲覧モードへ変更
        self.show_view_operation()

    # 削除ボタンが押された場合の処理
    def on_click_delete_button(self):
        # ユーザの選択を取得
        selection = self.diary_list.curselection()
        if not selection:
            return
        # データベースから削除
        index = selection[0]
        diary_id = self.date_list[index][0]
        self.db.delete_diary(diary_id=diary_id)
        # リストの内容をリロード
        self.reload_diary_list()

    # 日記リストをリロードする
    def reload_diary_list(self):
        # 要素を全て削除
        self.diary_list.delete(0, tk.END)
        # リストに日付を追加していく
        self.date_list = self.db.get_list()
        for date in self.date_list:
            self.diary_list.insert(tk.END, date[1])
        # リストの一番上を選択
        self.diary_list.select_set(0)
        self.on_diary_select()

    # 操作ボタンを閲覧モードのものに変える
    def show_view_operation(self):
        # 書き込み操作ボタンを隠し、閲覧操作ボタンを出す
        self.input_operation_frame.grid_remove()
        self.view_operation_frame.grid()

    # 操作ボタンを書き込みモードのものに変える
    def show_input_operation(self):
        # 閲覧操作ボタンを隠し、書き込み操作ボタンを出す
        self.view_operation_frame.grid_remove()
        self.input_operation_frame.grid()