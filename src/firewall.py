import tkinter as tk

from src.gui import FirewallGUI


def main():
    root = tk.Tk()

    app = FirewallGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()