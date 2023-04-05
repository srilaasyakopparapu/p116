# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Laasya" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "Siva" # write your name
    age = "45" # write your age

    return render_template('index.html' , name = name , age = age)

#def first_flask():
# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Deepthi" # write your name
    age = "40" # write your age

    return render_template('index.html' , name = name , age = age)

#def second_flask():
# define the route to friends webpage
@app.route("/friends")
def home():

    name = "Chloe" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

#def third_flask():
# add other routes, if you want




# run the file
if __name__ ==  '__main__':
    app.run(debug=True)
