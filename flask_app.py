from flask import Flask, redirect, url_for, request, render_template, abort

app = Flask(__name__)
app.debug = True
USER = {
    "user_name": "",
    "age": "",
    "phone": ""
}


def fail(fail_mesg, err_code=500, return_obj={}):
    fail = {
        "code": err_code,
        "message": fail_mesg,
        "return_obj": return_obj
    }
    return fail


def success(mesg, return_obj={}):
    done = {
        "code": 200,
        "message": f"success {mesg}",
        "return_obj": return_obj
    }
    return done


@app.route('/addUser', methods=["POST"])
def add_user():
    global USER
    user_info = request.json
    if not isinstance(user_info['phone'], str):
        return fail("not allow!!")
    USER['user_name'] = user_info['user_name']
    USER['age'] = user_info["age"]
    USER['phone'] = user_info["phone"]
    return success("add user", USER)


@app.route("/findUser/<string:name>")
def get_user_info(name):
    global USER
    user_info = {
        "mesg": "not people"
    }
    if name == USER['user_name']:
        user_info = {
            "user_name": USER['user_name'],
            "age": USER['age'],
            "phone": USER["phone"]
        }
    return success("", user_info)


@app.route("/delUser", methods=["POST"])
def del_user():
    name = request.json['user_name']
    return success(f"del {name} done")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=65525)
