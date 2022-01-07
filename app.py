from flask import Flask, Response, render_template, request
from frames_generator import screenshots
from wikipedia import get_revision_ids

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    query = None
    if request.method == 'POST':
        print(request.form.get('wikiquery'))
        query = request.form.get('wikiquery')
    return render_template('index.html', query=query)


@app.route('/wiki_feed/<title>')
def wiki_feed(title):
    revision_ids, timestamps = get_revision_ids(title)
    return Response(screenshots(title, revision_ids),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
