import tkinter as tk
counter=0
def counter_label(label):
    counter=0
    def count():
        global counter
        counter=counter+1
        label.config(text=str(counter))
        label.after(100,count)
        window.config(bg="pink")
    count()

window = tk.Tk()
window.title("COUNTER")
label=tk.Label(window,fg="red",background="lightblue",width=20)
label.pack(pady=30)
counter_label(label)
button=tk.Button(window, text="Stop", width=40, command=window.destroy)
button.pack(pady=30)
window.mainloop()
