import requests

def getLink(mail, link):
    a = requests.post("https://cheggbot.woosal.com/json.php", data={"mail":"{0}".format(mail),"soru":"{0}".format(link),"key":""})
    return a.text

