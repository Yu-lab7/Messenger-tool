#                                                                                             ##                        ###
                                                                                             ##                         ##
 ##  ##    ####     #####    #####    ####    #####     ### ##   ####    ######             #####    ####     ####      ##
 #######  ##  ##   ##       ##       ##  ##   ##  ##   ##  ##   ##  ##    ##  ##             ##     ##  ##   ##  ##     ##
 ## # ##  ######    #####    #####   ######   ##  ##   ##  ##   ######    ##                 ##     ##  ##   ##  ##     ##
 ##   ##  ##            ##       ##  ##       ##  ##    #####   ##        ##                 ## ##  ##  ##   ##  ##     ##
 ##   ##   #####   ######   ######    #####   ##  ##       ##    #####   ####                 ###    ####     ####     ####
                                                       #####

 ##   ##    ##     #####    #######           ######   ##  ##            ##  ##   ##   ##  ####       ##     ######            ######
 ### ###   ####     ## ##    ##   #            ##  ##  ##  ##            ##  ##   ##   ##   ##       ####     ##  ##           ##  ##
 #######  ##  ##    ##  ##   ## #              ##  ##  ##  ##            ##  ##   ##   ##   ##      ##  ##    ##  ##               ##
 #######  ##  ##    ##  ##   ####              #####    ####              ####    ##   ##   ##      ##  ##    #####   ######      ##
 ## # ##  ######    ##  ##   ## #              ##  ##    ##                ##     ##   ##   ##   #  ######    ##  ##             ##
 ##   ##  ##  ##    ## ##    ##   #            ##  ##    ##                ##     ##   ##   ##  ##  ##  ##    ##  ##             ##
 ##   ##  ##  ##   #####    #######           ######    ####              ####     #####   #######  ##  ##   ######              ##

import tkinter as tk
import pyautogui
import time
import threading

class SpamBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Messenger tool")
        self.root.geometry("400x400")
        self.root.config(bg="black")  # 背景色を黒に設定
        self.root.eval('tk::PlaceWindow . center')  # ウィンドウを画面中央に配置

        self.messages = []
        self.is_spamming = False

        # ターミナル風のフォントと色
        self.label = tk.Label(root, text="Enter your messages (one per line):", bg="black", fg="lime", font=("Courier", 10))
        self.label.pack(pady=10)

        # テキストボックスのカスタマイズ（黒背景、緑文字、モノスペースフォント）
        self.textbox = tk.Text(root, height=8, width=40, bg="black", fg="lime", insertbackground="lime", font=("Courier", 10), borderwidth=0)
        self.textbox.pack(pady=10)

        # インターバルラベルのカスタマイズ
        self.interval_label = tk.Label(root, text="Time interval (in seconds):", bg="black", fg="lime", font=("Courier", 10))
        self.interval_label.pack()

        # インターバル入力のカスタマイズ
        self.interval_entry = tk.Entry(root, bg="black", fg="lime", font=("Courier", 10), insertbackground="lime", borderwidth=0)
        self.interval_entry.pack(pady=5)

        # ボタンのカスタマイズ（黒背景、緑文字、モノスペースフォント）
        self.start_button = tk.Button(root, text="Start", command=self.start_spamming, bg="black", fg="lime", font=("Courier", 10), activebackground="green", activeforeground="black")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_spamming, bg="black", fg="lime", font=("Courier", 10), activebackground="red", activeforeground="black")
        self.stop_button.pack()

        # ラベルの点滅アニメーション
        self.blinking = True
        self.blink_label()

    def blink_label(self):
        if self.blinking:
            current_color = self.label.cget("fg")
            next_color = "black" if current_color == "lime" else "lime"
            self.label.config(fg=next_color)
            self.root.after(500, self.blink_label)

    def start_spamming(self):
        self.messages = self.textbox.get("1.0", tk.END).strip().split("\n")
        try:
            self.interval = float(self.interval_entry.get())
        except ValueError:
            print("Invalid interval. Please enter a number.")
            return

        if not self.messages or self.interval <= 0:
            print("Please enter valid messages and interval.")
            return

        self.is_spamming = True
        threading.Thread(target=self.spam_messages).start()

    def stop_spamming(self):
        self.is_spamming = False

    def spam_messages(self):
        while self.is_spamming:
            for message in self.messages:
                if not self.is_spamming:
                    break
                pyautogui.write(message)
                pyautogui.press("enter")
                time.sleep(self.interval)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamBotApp(root)
    root.mainloop()
