import unittest
from src.load_balancer import LoadBalancer
from src.server import Server


class TestLoadBalancer(unittest.TestCase):

    def setUp(self):
        self.servers = [Server(f"Server {i}", cpu_capacity=20) for i in range(3)]
        self.load_balancer = LoadBalancer(self.servers)

    def test_get_least_loaded_server(self):
        server = self.load_balancer.get_least_loaded_server(5)
        self.assertIn(server, self.servers)

    def test_distribute_load(self):
        requests = [("req1", 5), ("req2", 5), ("req3", 5), ("req4", 5), ("req5", 5), ("req6", 5)]
        self.load_balancer.distribute_load(requests)

        total_load = sum(server.get_load() for server in self.servers)
        self.assertEqual(total_load, sum(cpu_cost for _, cpu_cost in requests))

        # Verificar que la carga se distribuye de manera más equilibrada
        loads = [server.get_load() for server in self.servers]
        self.assertTrue(max(loads) - min(loads) <= 5)


if __name__ == "__main__":
    unittest.main()
