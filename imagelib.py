import base64
import requests
try:
    from StringIO import BytesIO
except ImportError:
    from io import BytesIO


def getBase64Image(url):
    b64 = base64.b64encode(requests.get(url).content)
    return b64.decode('utf-8')