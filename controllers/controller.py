from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
  return render_template('index.html', title='Book Orders', orders=orders)