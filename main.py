from router import Router
from switch import Switch


router1 = Router(
    "Huawei",
    "192.168.1.1",
    "Online",
    8
)


switch1 = Switch(
    "Cisco",
    "192.168.1.2",
    "Online",
    24
)


router1.display_info()

router1.restart()

switch1.display_info()

switch1.forward_packet()