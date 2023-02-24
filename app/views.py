from app import app
from flask import render_template, request
import os
import pandas as pd
import matplotlib.pyplot as plt


@app.route('/')
def index():
    # Get list of CSV files in the current directory
    csv_files = [file for file in os.listdir('dataset') if file.endswith('.csv')]
    return render_template('index.html', csv_files=csv_files)

@app.route('/proceed', methods=['POST'])
def proceed_data():
    file_name = request.form['csv_file']
    file_path = os.path.join('dataset', file_name)
    data = pd.read_csv(file_path)
    html_table = data.to_html(index=False)
    return render_template('data.html', table=html_table)