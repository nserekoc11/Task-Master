# Initializing the tkinter module
import tkinter as tk
root = tk.Tk()
root.title("Counter App")
root.geometry("300x300")
root.resizable(False, False)


greeting_label = tk.Label(root, text="Welcome to the Counter App!") 
greeting_label.pack(pady=20)

#counter app
countr = 0
while countr < 10:
    print (countr)
    countr += 1

root.mainloop()