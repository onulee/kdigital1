from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")


# User-Agent설정, 설정하지 않을시 HeadlessChrome 표시 됨.- 차단 당할수 있음 
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")

browser = webdriver.Chrome(options=options)

url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

txt_userAgent = browser.find_element_by_id("detected_value")
print(txt_userAgent.text)
print("-"*50)