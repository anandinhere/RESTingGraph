import flask
from flask import Flask, url_for

from flask import request

app = flask.Flask(__name__)



#class flask.request
# To access incoming request data, you can use the global request object. Flask parses incoming request data for you and gives you access to it through that global object. Internally Flask makes sure that you always get the correct data for the active thread if you are in a multithreaded environment.
#
# This is a proxy. See Notes On Proxies for more information.
#
#The request object is an instance of a Request subclass and provides all of the attributes Werkzeug defines. This just shows a quick overview of the most important ones.


#http://werkzeug.pocoo.org/docs/0.12/wrappers/#werkzeug.wrappers.AuthorizationMixin
##http://flask.pocoo.org/snippets/8/
@app.route("/", methods=['DELETE'])
def hello():
    print(type(request.headers['Authorization']))
    auth = request.authorization
    print(auth)
    #print request.environ
    print request.base_url
    return "Whatsup World!"

#http://flask.pocoo.org/docs/0.12/quickstart/
@app.route('/user/<username>', methods=['GET'])
def profile(username):
    print username

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


#Upload File
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print f
        f.save('.' + secure_filename(f.filename))
        return 'upload success'

if __name__ == '__main__':

    print('RUNNING WEB APP...')

    app.run(debug=True)
