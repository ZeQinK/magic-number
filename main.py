from flask import Flask, render_template, request 

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        first = request.form['digit1']
        second = request.form['digit2']
        third = request.form['digit3']
        forth = request.form['digit4']
        fifth = request.form['digit5']

        num_list = [first, second, third, forth, fifth]
        number = 0 

        for i in range(len(num_list)):
            if num_list[i] == "Yes":
                number += 2**(i) * 1
        
        return render_template("index.html", number = number)



if __name__ == "__main__":
    app.run()
