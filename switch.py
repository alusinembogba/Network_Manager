from network_device import NetworkDevice


class Switch(NetworkDevice):

    def __init__(self, brand, ip_address, status, ports):
        super().__init__(brand, ip_address, status)
        self.ports = ports


    def forward_packet(self):
        print(f"{self.brand} forwarding packets...")