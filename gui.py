import tkinter as tk
import main


def btn_start():
    text = entry.get()
    main.post_blog_by_keyword(text, spin_value.get(), radio_select())


def radio_select():
    selected = str(radio.get())
    return selected


root = tk.Tk()
root.title("blogBot")
root.geometry("250x300")

tk.Label(text="\n블로그 주제").pack()
entry = tk.Entry(root, width=30)
entry.pack()

tk.Label(text="\n포스팅 개수").pack()
spin_value = tk.IntVar()
spin_value.set(3)
spin = tk.Spinbox(root, from_=1, to=100, width=10, textvariable=spin_value)
spin.pack()

tk.Label(text="\n포스팅 설정").pack()
radio = tk.IntVar()

rad1 = tk.Radiobutton(root, text="공개", variable=radio, value=3, command=radio_select)
rad1.pack()
rad2 = tk.Radiobutton(root, text="비공개", variable=radio, value=0, command=radio_select)
rad2.pack()

tk.Label(text="\n").pack()
button = tk.Button(root, text="글쓰기 시작", command=btn_start)
button.pack()

root.mainloop()
