import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Album Chooser")
    root.resizable(False, False)

    scrollbar = ttk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    album_list = tk.Listbox(root, yscrollcommand= scrollbar.set)

    with open("albums.txt", "r+") as file:
        index = 0
        for line in file:
            album_list.insert(index, line.strip())
            index += 1

    album_list.pack(side="top", fill="both")
    scrollbar.config(command=album_list.yview)

    tk.mainloop()


if __name__ == "__main__":
    main()