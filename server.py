
from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)



@app.route("/")
def index():
    return redirect("/users")



@app.route("/users")
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", users=users)



from user import User
@app.route('/user/new')
def get_all_user():
    return render_template("new_users.html")



@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.save(data)

    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html", user=User.get_one(data))


@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    
    return render_template("show_user.html", user=User.get_one(data))


@app.route('/user/update/<int:id>', methods =['POST'])
def update(id):
    data = {
        "id":id,
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.update(data)
    return redirect('/users')


@app.route('/user/destroy/<int:id>')
def                                                                destroy(id):
    data ={
        "id": id
    }
    User.destroy(data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)