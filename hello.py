from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "Hi there!"

@app.route('/about_us')
def about_us():
    return "We are happy to help you! Thank You!"


if __name__=='__main__':
    app.run(debug=True)
