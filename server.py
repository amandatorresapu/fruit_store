from flask import Flask, render_template, request  # Import Flask to allow us to create our app
app = Flask(__name__)  

@app.route('/index')
def index():  
        print("showing index page")
        return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():  
        print("Got the post data")
        print(request.form)
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        return render_template("checkout.html", first_name = first_name, last_name = last_name)

@app.route('/checkout')
def checkout():
        return render_template("checkout.html")

@app.route('/fruits')
def fruits():
        return render_template("fruits.html")





if __name__=="__main__":   
    app.run(debug=True)    