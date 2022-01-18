from flask import Flask, Response, render_template, request
from frames_generator import screenshots
from wikipedia import get_random_title

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    query = None
    if request.method == 'POST':
        query = request.form.get('wikiquery')
    return render_template('index.html', query=query)


@app.route('/random', methods=["GET"])
def random_wiki_feed():
    return Response(screenshots(get_random_title),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/wiki_feed/<title>')
def wiki_feed(title):
    return Response(screenshots(title),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
