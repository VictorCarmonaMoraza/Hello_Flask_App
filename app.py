from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)


# Define a Route
@app.route('/')
def hello():
    return render_template('index.html', name="Flask Developer")

# Run the App
if __name__ == "__main__":
    ## En entorno de produccion no se pone debug=True
    app.run(debug=True)