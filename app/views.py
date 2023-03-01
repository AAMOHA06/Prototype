from app import app
from flask import render_template, request
import os
import pandas as pd
import matplotlib.pyplot as plt


@app.route('/')
def index():
    # Get list of CSV files in the current directory
    csv_files = []
    for root, dirs, files in os.walk('dataset'):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return render_template('index.html', csv_files=csv_files)


@app.route('/proceed', methods=['POST'])
def proceed():
    if request.method == 'POST':
        file_name = request.form['csv_file']
        file_path = os.path.abspath(os.path.join(file_name))
        data = pd.read_csv(file_path)
        print(file_path)
        headers = data.columns.tolist()
        rows = data.values.tolist()
        return render_template('data.html', headers=headers, rows=rows)