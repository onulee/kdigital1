import requests
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# res = requests.get("http://www.google.com")
res = requests.get("http://www.melon.com",headers=headers)
res.raise_for_status()
with open("melon.html","w",encoding="utf-8") as f:
    f.write(res.text)
print(res.text)
