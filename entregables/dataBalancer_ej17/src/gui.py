import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas
from tkinter import ttk  # Importa el submódulo ttk de tkinter para widgets temáticos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importa FigureCanvasTkAgg para integrar matplotlib con tkinter
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot para crear gráficos
import random  # Importa el módulo random para generar números aleatorios
import time  # Importa el módulo time para funciones relacionadas con el tiempo
from load_balancer import LoadBalancer  # Importa la clase LoadBalancer del módulo load_balancer
from server import Server  # Importa la clase Server del módulo server

class ServerMonitorApp:
    def __init__(self, root, servers):
        """
        Initialize the ServerMonitorApp.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            servers (list): A list of Server objects to be monitored.
        """
        self.root = root  # Asigna la ventana raíz de tkinter a un atributo de la clase
        self.servers = servers  # Asigna la lista de servidores a un atributo de la clase
        self.load_balancer = LoadBalancer(servers)  # Crea una instancia de LoadBalancer con la lista de servidores
        self.root.title("Server Load Monitor")  # Establece el título de la ventana

        # Crea una figura y ejes para los gráficos, uno por servidor más uno adicional
        self.fig, self.axs = plt.subplots(len(servers) + 1, 1, figsize=(12, 10))
        # Crea un widget de canvas para mostrar la figura en la ventana de tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)  # Empaqueta el canvas en la ventana

        # Crea un marco para mostrar información adicional
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)  # Empaqueta el marco en la ventana

        # Crea etiquetas para mostrar información de cada servidor
        self.info_labels = [tk.Label(self.info_frame, text="", font=("Helvetica", 14)) for _ in servers]
        for label in self.info_labels:
            label.pack(pady=10)  # Empaqueta cada etiqueta en el marco con un margen vertical

        # Crea una etiqueta para mostrar información de la cola de solicitudes pendientes
        self.queue_info_label = tk.Label(self.info_frame, text="", font=("Helvetica", 14))
        self.queue_info_label.pack(pady=10)  # Empaqueta la etiqueta en el marco con un margen vertical

        # Inicializa un diccionario para almacenar el historial de cargas de CPU de cada servidor
        self.cpu_loads_history = {server.name: [] for server in servers}
        # Inicializa una lista para almacenar el historial de cargas de CPU entrantes
        self.incoming_cpu_load_history = []

        self.update_graph()  # Llama al método para actualizar el gráfico

    def generate_random_requests(self):
        """
        Generate a list of random requests.

        Returns:
            list: A list of tuples representing requests. Each tuple contains a request ID, CPU cost, and another random value.
        """
        num_requests = random.randint(1, 40)  # Genera un número aleatorio de solicitudes
        # Crea una lista de tuplas con ID de solicitud, costo de CPU y otro valor aleatorio
        requests = [(f"req{random.randint(1, 1000)}", random.randint(1, 20), random.randint(1, 20)) for _ in range(num_requests)]
        return requests  # Devuelve la lista de solicitudes

    def update_graph(self):
        """
        Update the graph with the current server loads and incoming CPU load.
        """
        requests = self.generate_random_requests()  # Genera solicitudes aleatorias
        total_cpu_cost = sum(cpu_cost for _, cpu_cost, _ in requests)  # Calcula el costo total de CPU de las solicitudes
        self.incoming_cpu_load_history.append(total_cpu_cost)  # Agrega el costo total al historial de cargas de CPU entrantes

        self.load_balancer.distribute_load(requests)  # Distribuye las solicitudes entre los servidores
        self.load_balancer.process_pending_requests()  # Procesa las solicitudes pendientes

        for server in self.servers:
            self.cpu_loads_history[server.name].append(server.get_load())  # Agrega la carga actual de cada servidor a su historial

        for i, server in enumerate(self.servers):
            self.axs[i].clear()  # Limpia el gráfico del servidor
            self.axs[i].plot(self.cpu_loads_history[server.name], label=f"{server.name} CPU Load", linewidth=2)  # Dibuja el historial de cargas de CPU
            self.axs[i].set_ylim(0, server.cpu_capacity)  # Establece los límites del eje y
            self.axs[i].set_ylabel('CPU Load', fontsize=12)  # Establece la etiqueta del eje y
            self.axs[i].legend(loc='upper right', fontsize=12)  # Agrega una leyenda al gráfico

            # Actualiza la etiqueta de información del servidor con su carga actual y número de tareas
            self.info_labels[i].config(text=f"{server.name}\nCurrent Load: {server.get_load()}\nTasks: {len(server.requests)}")

        self.axs[-1].clear()  # Limpia el gráfico de cargas de CPU entrantes
        self.axs[-1].plot(self.incoming_cpu_load_history, label="Incoming CPU Load", linewidth=2)  # Dibuja el historial de cargas de CPU entrantes
        self.axs[-1].set_ylabel('CPU Load', fontsize=12)  # Establece la etiqueta del eje y
        self.axs[-1].legend(loc='upper right', fontsize=12)  # Agrega una leyenda al gráfico

        # Obtiene las solicitudes pendientes de la cola del balanceador de carga
        pending_requests = list(self.load_balancer.pending_requests.queue)
        pending_count = len(pending_requests)  # Cuenta el número de solicitudes pendientes
        pending_cpu_cost = sum(cpu_cost for _, _, cpu_cost in pending_requests)  # Calcula el costo total de CPU de las solicitudes pendientes
        # Actualiza la etiqueta de información de la cola con el número de solicitudes pendientes y su costo total de CPU
        self.queue_info_label.config(text=f"Pending Requests: {pending_count}\nTotal CPU Cost: {pending_cpu_cost}")

        self.canvas.draw()  # Redibuja el canvas con los gráficos actualizados

        for server in self.servers:
            server.reset_load()  # Resetea la carga del servidor
            server.reset_cpu_processed_per_turn()  # Resetea el CPU procesado por turno del servidor

        self.root.after(1000, self.update_graph)  # Programa la próxima actualización del gráfico en 1 segundo

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana raíz de tkinter
    servers = [Server(f"Server {i}", cpu_capacity=100) for i in range(3)]  # Crea una lista de servidores con capacidad de CPU de 100
    app = ServerMonitorApp(root, servers)  # Crea una instancia de ServerMonitorApp con la ventana raíz y la lista de servidores
    root.mainloop()  # Inicia el bucle principal de la aplicación tkinter