from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hotspots')
def hotspots():
    return render_template('hotspots.html')


@app.route('/recommendations')
def recommendations():
    df = pd.read_csv("recommendations.csv")

    table = df.to_html(classes='table table-striped')

    return render_template(
        "recommendations.html",
        table=table
    )

@app.route('/predictions')
def predictions():

    df = pd.read_csv("predictions.csv")

    table = df.head(20).to_html(classes='table table-striped')

    return render_template(
        'predictions.html',
        table=table
    )

if __name__ == '__main__':
    app.run(debug=True)