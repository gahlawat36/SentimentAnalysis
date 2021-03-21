# importing Flask and other modules 
from flask import Flask, request, render_template
from prediction import predictions

app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function 
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # get summary text from the input
        summary = request.form.get("summary")
        # get review text from the input
        review = request.form.get("review")

        # use prediction function to get final sentiment value
        answer = predictions(review, summary)
        sentiment = str(answer[0])
        if sentiment == '1':
            return 'That looks like  a positive review'
        else:
            return 'Oops that review doesnt sound good'
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)