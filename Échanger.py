from flask import Flask

# Initialisation de l'application web
app = Flask(__name__)

# Définition de la page principale (l'interface)
@app.route('/')
def home():
    # Code HTML de l'interface qui gère l'affichage et la redirection
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="0; url=https://link-hub.net/2633396/gpJ5h5q7GVZ6">
        <title>Interface de Redirection</title>
        <style>
            /* Style de l'interface en Python/HTML */
            body {
                background-color: #121212;
                color: #ffffff;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 40px;
                border: 2px solid #333;
                border-radius: 10px;
                background-color: #1e1e1e;
                box-shadow: 0 4px 8px rgba(0,0,0,0.5);
            }
            a {
                color: #4CAF50;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Chargement en cours...</h1>
            <p>Connexion établie. Vous allez être redirigé vers la destination.</p>
            <p>Si la redirection automatique ne s'active pas, <a href="https://link-hub.net/2633396/gpJ5h5q7GVZ6">cliquez directement ici</a>.</p>
        </div>
    </body>
    </html>
    """
    return html_content

# Lancement du serveur Python
if __name__ == '__main__':
    print("Démarrage de l'interface en Python...")
    print("Le serveur est accessible et prêt à rediriger.")
    # Le serveur tourne sur le port 8000
    app.run(host='0.0.0.0', port=8000)
