from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

dataframes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_data', methods=['POST'])
def load_data():
    try:
        file = request.files['file']
        if file:
            df = pd.read_csv(file)
            filename = file.filename
            dataframes[filename] = df
            shape = df.shape
            num_columns = shape[1]
            num_rows = shape[0]
            columns = df.columns.tolist()
            return jsonify({"num_columns": num_columns, "num_rows": num_rows, "columns": columns})
        else:
            return jsonify({"message": "No file uploaded", "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": "An error occurred while loading data", "status": "fail", "error": str(e)}), 500

@app.route('/analyze_data', methods=['POST'])
def analyze_data():
    try:
        data = request.json

        if 'file_id' not in data:
            return jsonify({"message": "Invalid request data", "status": "fail"}), 400

        filename = data['file_id']

        if filename not in dataframes:
            return jsonify({"message": "File not found", "status": "fail"}), 404

        df = dataframes[filename]

        numerical_stats = df.describe().to_dict()

        return jsonify({"num_columns": len(df.columns), "num_rows": len(df), "numerical_stats": numerical_stats, "message": "Data analyzed successfully", "status": "success"})

    except Exception as e:
        return jsonify({"message": "An error occurred during data analysis", "status": "fail", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
