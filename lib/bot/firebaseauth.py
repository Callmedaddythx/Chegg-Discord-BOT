from firebase import firebase

firebase = firebase.FirebaseApplication('FIREBASELINK', None)


# Post
def addUser(userid, mail):
    data = {'mail': f'{mail}'}
    result = firebase.put(f"users/", userid, data)
    return result


def getUser(userid):
    result = firebase.get('/users/', userid)
    return result
    # returns {'mail': 'random@protonmail.com'}


def getUserMail(userid):
    result = firebase.get("/users/", userid)
    return result["mail"]
    # Returns the "user@mail.com"


def updateMail(userid, mail):
    data = {'mail': f'{mail}'}
    result = firebase.put(f"users/", userid, data)
    return result


def deleteUser(userid):
    result = firebase.delete("/users/", userid)
    return result
