from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Для роботи з сесіями

@app.route('/')
def index():
    # Ініціалізуємо баланс якщо його немає
    if 'balance' not in session:
        session['balance'] = 0
    return render_template('index.html', balance=session['balance'])

@app.route('/earn', methods=['POST'])
def earn():
    # Додаємо 5 євро до балансу
    if 'balance' not in session:
        session['balance'] = 0
    session['balance'] += 5
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
