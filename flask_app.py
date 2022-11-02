from flask import Flask, redirect, url_for, request, render_template, abort

app = Flask(__name__)
app.debug = True
USER = {
    "username": "testFindName",
    "age": "25",
    "phone": "1358xxxxxxxx"
}


def fail(failMesg, errCode=500, returnObj={}):
    fail = {
        "code": errCode,
        "message": failMesg,
        "returnObj": returnObj
    }
    return fail


def success(mesg, returnObj={}):
    done = {
        "code": 200,
        "message": f"success {mesg}",
        "returnObj": returnObj
    }
    return done


@app.route('/addUser', methods=["POST"])
def addUser():
    global USER
    userInfo = request.json
    if not isinstance(userInfo['phone'], str):
        return fail("not allow!!")
    USER['username'] = userInfo['username']
    USER['age'] = userInfo["age"]
    USER['phone'] = userInfo["phone"]
    return success("add user", USER)


@app.route("/findUser/<string:name>")
def getUserInfo(name):
    global USER
    user_info = {
        "mesg": "not people"
    }
    if name == USER['username']:
        user_info = {
            "username": USER['username'],
            "age": USER['age'],
            "phone": USER["phone"]
        }
    return success("", user_info)


@app.route("/delUser", methods=["POST"])
def delUser():
    name = request.json['username']
    return success(f"del {name} done")


if __name__ == '__main__':
    app.run()
