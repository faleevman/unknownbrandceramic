import requests
import shutil
import uuid
url = "https://ipfs.io/ipfs/{}"

def get_ipfs(hash):
    print("Hash", hash)
    h = name = uuid.uuid4().hex
    r = requests.get(url.format(hash), stream=True)
    with open("12345.png", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
    return "12345" + ".png"
