import os
import threading


class Network(object):
	"""Class para definição da rede"""
	def __init__(self, ip, mask='255.255.255.0'):
		self.ip = ip
		self.mask = mask
		self.networks = []

	def __str__(self):
		return 'IP: {0}\nNetwork:\n{1}'.format(self.ip, self.networks)

	def check_ip(self):
		ip_list = self.ip.split('.')
		count = 0
		if len(ip_list) == 4:
			for octal in ip_list:
				if octal.isnumeric():
					count += 1
					if count == 4:
						self.ip = ip_list
						return True
					else: 
						continue
				else:
					return False
		return False

	def _scan(self, command, lock):
		test = os.popen(command).read()
		if "TTL" in test:
			with lock:
				self.networks.append(command[5:-10])
		else:
			return
	
	def set_networking(self):
		trheads = []
		lock = threading.Lock()
		value = self.mask.count('0')
		match value:
			case 1:
				for interval in range(1, 255):
					t = threading.Thread(target=self._scan, args=(f"ping {self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{interval} -n 1 -w 1", lock))
					t.start()
					trheads.append(t)
				for thread in trheads:
					thread.join()
			case 2:
				# Analisar redes maiores
				pass

