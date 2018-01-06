import flask
from flask import Flask, url_for

from flask import request

app = flask.Flask(__name__)

@app.route("/", methods=['DELETE'])
def hello():
    print(type(request.headers['Authorization']))
    auth = request.authorization
    print(auth)
    return "Whatsup World!"

@app.route('/user/<username>', methods=['GET'])
def profile(username): pass

#Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

#URL Building
with app.test_request_context():
    print(url_for('hello'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':

    print('RUNNING WEB APP...')

    app.run(debug=True)
