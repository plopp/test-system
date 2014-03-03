from ddp.client import DdpClient
client = DdpClient('127.0.0.1:3000')
client.connect()
try:
    client.method('sayHello',["System_XX","10.90.1.1"], timeout=2)
except:
    pass
client.disconnect()
