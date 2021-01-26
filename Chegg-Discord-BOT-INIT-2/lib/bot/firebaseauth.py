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

def addQuestion(userid, questionid):
    if getUser(userid) != None:

        result = firebase.put("users/", f"{userid}/question", questionid)
        return result
    else:
        return "Such user does not exist!"

def updateQuestion(userid, questionid):
    if getUser(userid) != None:

        result = firebase.put("users/", f"{userid}/question", questionid)
        return result
    else:
        return "Such user does not exist!"

def getQuestion(userid):
    if getUser(userid) != None:
        result = firebase.get("/users/", userid)
        return result["question"]
    else:
        return "Such user does not exist!"

def deleteQuestion(userid):
    if getUser(userid) != None:
        result = firebase.put("users/", f"{userid}/question", "")
        return result

def getUIDByQuestionID(questionid):
    dict = firebase.get("/users/",None)
    for i in firebase.get("/users/",None):
        user = dict[i]
        que = user["question"]
        if que == questionid:
            return i
