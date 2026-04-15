from flask import Flask, render_template

app = Flask(__name__)

# Route principale pour afficher ton site
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Le mode debug permet de voir les erreurs en direct
    app.run(debug=True)
