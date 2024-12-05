class Server:
    def __init__(self, name, cpu_capacity):
        """
        Initialize the Server.

        Args:
            name (str): The name of the server.
            cpu_capacity (int): The total CPU capacity of the server.
        """
        self.name = name
        self.cpu_capacity = cpu_capacity  # Capacidad total de CPU
        self.cpu_load = 0  # Carga actual de CPU
        self.total_cpu_processed = 0  # Total de CPU procesada
        self.cpu_processed_per_turn = 0  # CPU procesada por turno
        self.requests = []

    def handle_request(self, request, cpu_cost):
        """
        Handle a request by adding its CPU cost to the server's load.

        Args:
            request (str): The request ID.
            cpu_cost (int): The CPU cost of the request.
        """
        if self.cpu_load + cpu_cost <= self.cpu_capacity:
            self.cpu_load += cpu_cost
            self.total_cpu_processed += cpu_cost
            self.cpu_processed_per_turn += cpu_cost
            self.requests.append(request)
        else:
            print(f"Server {self.name} cannot handle request {request} due to insufficient CPU capacity")

    def get_load(self):
        """
        Get the current CPU load of the server.

        Returns:
            int: The current CPU load.
        """
        return self.cpu_load

    def reset_load(self):
        """
        Reset the CPU load of the server to zero and clear the requests.
        """
        self.cpu_load = 0
        self.requests.clear()

    def reset_cpu_processed_per_turn(self):
        """
        Reset the CPU processed per turn to zero.
        """
        self.cpu_processed_per_turn = 0

    def can_handle(self, cpu_cost):
        """
        Check if the server can handle a request with the given CPU cost.

        Args:
            cpu_cost (int): The CPU cost of the request.

        Returns:
            bool: True if the server can handle the request, False otherwise.
        """
        return self.cpu_load + cpu_cost <= self.cpu_capacity

    def get_total_cpu_processed(self):
        """
        Get the total CPU processed by the server.

        Returns:
            int: The total CPU processed.
        """
        return self.total_cpu_processed

    def get_cpu_processed_per_turn(self):
        """
        Get the CPU processed by the server in the current turn.

        Returns:
            int: The CPU processed in the current turn.
        """
        return self.cpu_processed_per_turn