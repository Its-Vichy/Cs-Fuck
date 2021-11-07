from client.client import Client
import sys, pymem

"""The client can be accessed by every extensions like this."""
try:
    client = Client()
except pymem.exception.ProcessNotFound as e:
    print(e)
    sys.exit()