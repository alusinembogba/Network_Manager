class NetworkDevice:

    def __init__(self, brand, ip_address, status):
        self.brand = brand
        self.ip_address = ip_address
        self.status = status

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"IP Address: {self.ip_address}")
        print(f"Status: {self.status}")