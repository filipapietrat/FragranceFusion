from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')

    # Assuming you have a CSV file named 'perfumes.csv' with columns 'name', 'brand', 'description'
    results = []
    with open('perfumes_with_images_partial.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if query.lower() in row['name'].lower() or query.lower() in row['brand'].lower() or query.lower() in row['description'].lower():
                results.append(row)

    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
