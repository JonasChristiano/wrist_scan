from threading import Lock, Thread
from colorama import Fore
from datetime import datetime
import socket
# import pyfiglet


class wrist(object):
	def __init__(self, **kwargs):
		self._ip = kwargs['ip']
		self._ports = kwargs['port']
		self._all_port = kwargs['all']
		self.data = {}

	def scann(self):
		threading = []
		lock = Lock()
		if self._all_port:
			for port in range(1,65537):
				t = Thread(target=self._port_scan, args=(port, lock))
				t.start()
				threading.append(t)
			for thread in threading:
				thread.join()
		elif self._ports:
			for port in self._ports:
				t = Thread(target=self._port_scan, args=(port, lock))
				t.start()
				threading.append(t)
			for thread in threading:
				thread.join()
		else:
			return "Error: Port do not found!"

	def _port_scan(self, port, lock):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(3)
		with lock:
			if s.connect_ex((self._ip, port)) == 0:
				try:
					data = s.recv(1024).decode()
					self.data[f"{port}"] = data
					s.close()
				except:
					self.data[f"{port}"] = "OPEN"
					s.close()
			

