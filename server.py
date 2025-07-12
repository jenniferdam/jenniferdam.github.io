import http.server
import socketserver
import os

ip = '192.168.1.39'
ruta = r'C:\Users\Linu\Desktop\something'
os.chdir(ruta)
#    Server information
adresses = (ip,8000)
handler = http.server.SimpleHTTPRequestHandler
httpp = socketserver.TCPServer(adresses,handler)

#   Open server
try:
    #   Catch default .html >> index.html
    print("server running!")
    httpp.serve_forever()
    
except KeyboardInterrupt:
    httpp.server_close()
    print("server closed")
