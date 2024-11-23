from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Galeria de fotos
@app.route('/gallery')
def gallery():
    fotos = [
        {"src": "/static/images/foto1.jpg", "alt": "Descrição 1"},
        {"src": "/static/images/foto2.jpg", "alt": "Descrição 2"},
        {"src": "/static/images/foto3.jpg", "alt": "Descrição 3"},
    ]
    return render_template('gallery.html', fotos=fotos)

# Página de contato
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form['nome']
        mensagem = request.form['mensagem']
        # Aqui você pode salvar a mensagem no banco ou enviar por email
        print(f"Mensagem recebida de {nome}: {mensagem}")
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
