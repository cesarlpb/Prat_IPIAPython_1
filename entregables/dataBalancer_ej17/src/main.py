import tkinter as tk
from gui import ServerMonitorApp
from server import Server

def main():
    """
    Main function to initialize and run the ServerMonitorApp.

    This function creates the root Tkinter window, initializes a list of Server objects,
    creates an instance of ServerMonitorApp with the root window and the list of servers,
    and starts the Tkinter main loop.
    """
    root = tk.Tk()
    servers = [Server(f"Server {i}", cpu_capacity=100) for i in range(3)]
    app = ServerMonitorApp(root, servers)
    root.mainloop()

if __name__ == "__main__":
    main()