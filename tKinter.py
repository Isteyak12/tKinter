import tkinter as tk
import subprocess

def run_another_file():
    output_window = tk.Toplevel()
    output_window.title("Output Window")

    output_text = tk.Text(output_window, height=20, width=50)
    output_text.pack()

    process = subprocess.Popen(
        ['python', 'app.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
        shell=True
    )

    def update_output():
        while True:
            line = process.stdout.readline()
            if not line:
                break
            output_text.insert(tk.END, line)
            output_text.see(tk.END)
            output_text.update_idletasks()

    output_window.after(100, update_output)

def start_gui():
    root = tk.Tk()
    root.title("GUI Launcher")
    
    button = tk.Button(root, text="Run Another File", command=run_another_file)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    start_gui()
