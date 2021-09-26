import requests
import shutil
url = "https://ipfs.io/ipfs/{}"

def get_ipfs(hash):
    print("Hash", hash)
    response = requests.get(url.format(hash), stream=True)
    return response.raw
