from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/app')
def map():
    return '<iframe width="100%" height="100%" frameborder="0" src="https:/zahkhaa.carto.com/builder/b111251f-8cd8-4ea8-8838-02d4e67a7446/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>'

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/lda')
def lda():
  return render_template('topicModelingVis.html')

if __name__ == "__main__":
	app.run(debug=True)
