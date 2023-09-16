from flask import Flask, render_template, request, redirect, url_for,flash,session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample user data (you should use a database in a real application)
users = [
    {'name': 'John', 'country': 'USA', 'email': 'john@gmail.com', 'password': 'password123'},
    {'name': 'Alice', 'country': 'Canada', 'email': 'alice@gmail.com', 'password': 'secret456'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        email = request.form['email']
        password = request.form['password']
        
        # Store the user data (in-memory storage, use a database in a real app)
        users.append({'name': name, 'country': country, 'email': email, 'password': password})
        
        return redirect(url_for('login'))  # Redirect to the login page after signup
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user exists (simplified check, should use a database)
        for user in users:
            if user['email'] == email and user['password'] == password:
                return render_template('welcome.html')
        
        flash('Login failed. Please check your email and password.')
    
    return render_template('login.html')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
