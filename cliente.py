from socket import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Operações disponíveis: sum, sub, mul, div")
op = input("Operation to invoke: ")
v1 = int(input("Enter 1st operand: "))
v2 = int(input("Enter 2nd operand: "))

data = {"OP": op, "V1": v1, "V2": v2}
msg = pickle.dumps(data)
s.send(msg)

msg = s.recv(1024)
data = pickle.loads(msg)

if data["STATUS"] == "OK":
    print("Result:", data["RES"])
else:
    print("Erro:", data["RES"])

s.close()
