# Data Analysis API

This is a simple Flask API project for uploading and analyzing CSV files.

## Usage

### Website API

1. Clone the repository:

git clone https://github.com/your-username/data-analysis-api.git

2. Navigate to the project directory:

cd data-analysis-api

3. Install the required dependencies:

pip install flask pandas

4. Run the Flask app:

python app.py

5. Access the API from your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Curl Command (Command Line)

Upload a CSV file using curl:

curl -X POST -F "file=@path/to/your/file.csv" http://127.0.0.1:5000/load_data

Replace path/to/your/file.csv with the actual path to your CSV file.

## Endpoints

- **`/`**: Home endpoint, displays a message indicating that the Data Analysis API is running.
- **`/load_data`**: POST endpoint for uploading a CSV file. Returns information about the uploaded data.
- **`/analyze_data`**: POST endpoint for analyzing the uploaded CSV data. Returns numerical statistics and data summary.

## Dependencies

- Flask
- pandas

## Dataset
The dataset used in this project is available on Kaggle at [Mall Customers Dataset](https://www.kaggle.com/datasets/aajay20/mall-customers-datacsv).
