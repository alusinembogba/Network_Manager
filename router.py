from network_device import NetworkDevice


class Router(NetworkDevice):

    def __init__(self, brand, ip_address, status, ports):
        super().__init__(brand, ip_address, status)
        self.ports = ports


    def restart(self):
        print(f"Restarting {self.brand} router...")
        self.status = "Online"
        print("Router back online.")