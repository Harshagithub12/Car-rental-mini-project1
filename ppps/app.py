# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a more secure key in a production environment

# In-memory list to store car and rental information
cars = [
    {"name": "Toyota", "model": "Camry", "year": 2022},
    {"name": "Honda", "model": "Civic", "year": 2021},
    {"name": "Ford", "model": "Mustang", "year": 2020},
    {"name": "Chevrolet", "model": "Malibu", "year": 2021},
    {"name": "Nissan", "model": "Altima", "year": 2022},
]

rentals = []

@app.route('/')
def index():
    return render_template('index.html', cars=cars, rentals=rentals)

@app.route('/rental-form')
def rental_form():
    return render_template('rental_form.html', cars=cars)

@app.route('/submit-rental', methods=['POST'])
def submit_rental():
    if request.method == 'POST':
        name = request.form['name']
        selected_car = request.form['car']
        action = request.form['action']

        rental_info = {'name': name, 'car': selected_car, 'action': action}

        # Store or update rental information
        if action == 'rent':
            rentals.append(rental_info)
            flash(f"Rental request submitted for {name} - {selected_car}")
        elif action == 'return':
            # Find and update the corresponding rental information
            for rental in rentals:
                if rental['name'] == name and rental['car'] == selected_car and rental['action'] == 'rent':
                    rental['action'] = 'return'
                    flash(f"Car returned by {name} - {selected_car}")
                    break

        return redirect(url_for('rental_form'))

if __name__ == '__main__':
    app.run(debug=True)
