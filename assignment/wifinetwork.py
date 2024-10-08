import network
import secrets
from time import sleep

class WiFi:
    def __init__(self):
        self.ssid = secrets.ssid
        self.password = ""
    
    def ConnectWiFi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Pico Connected on IP {ip}')
        return ip
