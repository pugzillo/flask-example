from flask import Flask, render_template, url_for, request, jsonify, Response #import everyting from template
import pickle
import pandas as pd

app = Flask(__name__)

posts = [
    {
        'author': 'Linh Chau',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 28, 2019'
    },
    {
        'author': 'George Washington',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 28, 2019'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts =posts)

@app.route('/about')
def about():
    return '<h1>I made an about page!</h1>'
    return render_template('about.html')

@app.route('/mpg')
def mpg():
    return render_template('mpg.html')

model=pickle.load(open('linreg.p', 'rb'))

@app.route('/inference',  methods = ['POST'])
def inference():
    req = request.get_json()
    print(req)
    c,h,w = req['cylinders'],req['horsepower'],req['weight']
    prediction = list(model.predict([[c,h,w]]))
    return jsonify({'c':c,'h': h,'w':w,'prediction':prediction[0] })

@app.route('/plot',  methods = ['GET'])
def plot():
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg,df.weight))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    




