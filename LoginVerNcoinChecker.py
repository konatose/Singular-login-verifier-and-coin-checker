import aminofix
from aminofix.lib.util.exceptions import *
from aminofix import Client
from aminofix import SubClient
import os
import hmac
from hashlib import sha1
from webbrowser import open as OP

os.system("CLS")

identifier = os.urandom(20)
x= ("19" + identifier.hex() + hmac.new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"), b"\x19" + identifier, sha1).hexdigest()).upper()
devi = x
client = Client(deviceId = x)

email = input("[Email]]::: ")
password = input("[Password]]::: ")

try:
    client.login(email,password)
except VerificationRequired as e:
    OP(e.args[0]["url"])
    print(e.args[0]["url"])

coins = int(client.get_wallet_info().totalCoins)
print( f"Total coins:- {coins}\n")
