import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    
    if uploaded_file.filename != '':
        # Save the uploaded file
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        
        # Load the data from the Excel file
        df = pd.read_excel(file_path)

        # Create a simple scatter plot (you can modify this based on your needs)
        plt.scatter(df['X'], df['Y'])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Scatter Plot')
        plot_filename = 'scatter_plot.png'
        plt.savefig(plot_filename)
        plt.show()
        
        # Return the plot as a downloadable file
        return send_file(plot_filename, as_attachment=True)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=False)
