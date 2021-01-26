import requests

def getLink(mail, link):
    f = open(r"C:\Users\woosal\Desktop\Chegg BOT X\Chegg-Discord-BOT-INIT-2\lib\bot", "r")
    secretkey = f.readline()
    f.close()

    a = requests.post("https://cheggbot.woosal.com", data={"mail":"{0}".format(mail),"soru":"{0}".format(link),"key":f"{secretkey}"})
    return a.text
