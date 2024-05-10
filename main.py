
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the routes for each page
@app.route('/about')
def about():
    # Render the about.html file for the "About" page
    return render_template('about.html')

@app.route('/services')
def services():
    # Render the services.html file for the "Services" page
    return render_template('services.html')

@app.route('/reviews')
def reviews():
    # Render the reviews.html file for the "Reviews" page
    return render_template('reviews.html')

@app.route('/photos')
def photos():
    # Render the photos.html file for the "Photos" page
    return render_template('photos.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
