import subprocess
import tkinter as tk

def run_human():
    subprocess.run(["python", "snake_game_human.py"])
    main()

def run_q_learning():
    subprocess.run(["python", "agent.py"])
    main()

def run_heuristic():
    subprocess.run(["python", "heuristic_plot_agent.py"])
    main()

def center_window(window, width=400, height=350):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def main():
    window = tk.Tk()
    window.title("🐍 Snake AI Launcher")
    center_window(window)
    window.configure(bg='#E0F7FA')

    title = tk.Label(window, text="בחר מצב משחק", font=("Segoe UI", 18, "bold"), bg='#E0F7FA', fg='#006064')
    title.pack(pady=20)

    def styled_button(master, text, command, color):
        return tk.Button(
            master,
            text=text,
            font=("Segoe UI", 12, "bold"),
            command=lambda:[window.destroy(), command()],
            width=30,
            pady=10,
            bg=color,
            fg='white',
            activebackground='#004D40',
            activeforeground='white',
            bd=0,
            relief='flat',
            highlightthickness=0,
            cursor='hand2'
        )

    styled_button(window, "🎮 שחקנית אנושית (Play)", run_human, '#26C6DA').pack(pady=10)
    styled_button(window, "🤖 AI - Q-Learning", run_q_learning, '#29B6F6').pack(pady=10)
    styled_button(window, "🧠 AI - Heuristics", run_heuristic, '#AB47BC').pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    main()
