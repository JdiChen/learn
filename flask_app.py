from flask import Flask, redirect, url_for, request, render_template,abort

app = Flask(__name__)
app.debug = True

def fail(fail_mesg):
    fail = {
        "code": 500,
        "error_mesg": fail_mesg
    }
    return fail


def success(mesg):
    done = {
        "code": 200,
        "message": f"success get {mesg}"
    }
    return done


@app.route('/test', methods=["POST"])
def test():
    name = request.json['myname']
    if name == "cq":
        abort(404,fail("not allow!!"))
        return fail("not allow!!")
    return success(name)


@app.route("/var/<string:show>/")
def get_var(show):
    return "get " + show


if __name__ == '__main__':
    app.run(debug=True)
