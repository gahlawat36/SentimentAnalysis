# importing Flask and other modules 
from flask import Flask, request, render_template
from processing import text_processing
from prediction import predictions
# Flask constructor 
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function 
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        summary = request.form.get("summary")
        # getting input with name = lname in HTML form
        review = request.form.get("review")

        answer = predictions(review, summary)
        sentiment = str(answer[0])
        if sentiment == '1':
            return 'That looks like  a positive review'
        else:
            return 'Oops that review doesnt sound good'
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)