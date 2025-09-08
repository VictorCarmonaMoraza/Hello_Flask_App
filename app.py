from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)


# Define a Route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

##Ruta de saludo
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

# ⚡ Ruta de error 404 personalizada
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the App
if __name__ == "__main__":
    ## En entorno de produccion no se pone debug=True
    app.run(debug=True)