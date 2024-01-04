import tkinter as tk

def fade_in(window, alpha=0.0, delta=0.01):
    if alpha < 1.0:
        alpha += delta
        window.attributes("-alpha", alpha)
        window.after(10, fade_in, window, alpha, delta)

def fade_out(window, alpha=1.0, delta=-0.01):
    if alpha > 0.0:
        alpha += delta
        window.attributes("-alpha", alpha)
        window.after(10, fade_out, window, alpha, delta)
    else:
        window.destroy()

def main():
    root = tk.Tk()
    root.title("Fade In/Out Animation")

    # Set initial transparency to 0
    root.attributes("-alpha", 0.0)

    # Set window size and position
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Call fade_in after a delay (e.g., 1000 milliseconds)
    root.after(1000, fade_in, root)

    # Button to trigger fade-out animation and destroy the window
    fade_out_button = tk.Button(root, text="Fade Out", command=lambda: fade_out(root))
    fade_out_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
