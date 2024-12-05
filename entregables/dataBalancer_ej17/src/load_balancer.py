from queue import PriorityQueue


class LoadBalancer:
    def __init__(self, servers):
        """
        Initialize the LoadBalancer.

        Args:
            servers (list): A list of Server objects to be managed by the load balancer.
        """
        self.servers = servers
        self.pending_requests = PriorityQueue()

    def get_least_loaded_server(self, cpu_cost):
        """
                Get the server with the least load that can handle the given CPU cost.

                Args:
                    cpu_cost (int): The CPU cost of the request.

                Returns:
                    Server: The server with the least load that can handle the request, or None if no server can handle it.
                """
        suitable_servers = [server for server in self.servers if server.can_handle(cpu_cost)]
        if not suitable_servers:
            return None
        return min(suitable_servers, key=lambda server: server.get_load())

    def distribute_load(self, requests):
        """
        Distribute incoming requests to the servers.

        Args:
            requests (list): A list of tuples representing requests. Each tuple contains a request ID, CPU cost, and priority.
        """
        for request, cpu_cost, priority in requests:
            self.pending_requests.put((priority, request, cpu_cost))

        self.process_pending_requests()

    def process_pending_requests(self):
        """
        Process pending requests by assigning them to the least loaded server that can handle them.
        """
        while not self.pending_requests.empty():
            priority, request, cpu_cost = self.pending_requests.get()
            server = self.get_least_loaded_server(cpu_cost)
            if server:
                server.handle_request(request, cpu_cost)
            else:
                self.pending_requests.put((priority, request, cpu_cost))
                break
