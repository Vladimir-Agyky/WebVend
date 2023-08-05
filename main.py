from flask import Flask, render_template, Blueprint, request
from module.test_module import test_module
import pandas as pd
from flask import Blueprint, render_template, request

# import config as config

def read_txt_file(file_path):
    stock_numbers = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        stock_numbers = len(lines)
        items = [(index + 1, line.strip()) for index, line in enumerate(lines)]

    return stock_numbers, items


app = Flask(__name__)

app.register_blueprint(test_module)

# app.config.from_object('config')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shop")
def shop():
    file_path = "stocks.txt"
    num_rows, items = read_txt_file(file_path)
    return render_template('shop.html', items=items, num_rows=num_rows)

@app.route("/search_license")
def contact():
    return render_template('search.html')

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8081" ,debug=True)