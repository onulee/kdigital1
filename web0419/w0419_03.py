import requests
# res = requests.get("http://www.google.com")
res = requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
res.raise_for_status()
with open("detected_value.html","w","utf-8") as f:
    f.write(res.text)
print(res.text)
