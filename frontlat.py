from flask import Flask, render_template, request, send_from_directory
import tes as tes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('awal.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.1.2.3', port=1234)