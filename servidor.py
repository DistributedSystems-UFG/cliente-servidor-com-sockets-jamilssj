from socket  import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind(("0.0.0.0", PORT))
s.listen(1)
print(f"Servidor esperando conexões em {HOST}:{PORT} ...")
(conn, addr) = s.accept()
print(f"Cliente conectado: {addr}")

while True:
    msg = conn.recv(1024)
    if not msg: 
        break
    data = pickle.loads(msg)
    print("Recebido:", data)

    op = data["OP"]
    v1 = data["V1"]
    v2 = data["V2"]

    if op == "sum":
        res = v1 + v2
        status = "OK"
    elif op == "sub":
        res = v1 - v2
        status = "OK"
    elif op == "mul":
        res = v1 * v2
        status = "OK"
    elif op == "div":
        if v2 != 0:
            res = v1 / v2
            status = "OK"
        else:
            res = "Divisão por zero!"
            status = "NOK"
    else:
        res = 1
        status = "NOK"

    data = {"STATUS": status, "RES": res}
    msg = pickle.dumps(data)
    conn.send(msg)

conn.close()
