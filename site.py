from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='', static_folder='')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///products.db'

database = SQLAlchemy(app, session_options={'expire_on_commit': False})

class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    image = database.Column(database.String(200), nullable=False)
    name = database.Column(database.String(100), nullable=False)
    price = database.Column(database.String(100), nullable=False)

products=[]

product= Product(image='https://lr.ru/images/lr/LETTER-bI-RUS-GBL__20.jpg', name='буква Ы', price='8')

if product not in products:
    products.append(product)

with app.app_context():
    database.create_all()
    database.session.add(product)
    database.session.commit()

@app.route('/')
def index():
    context=product
    print(context.image)
    return render_template('index.html', context=context)

if __name__=='__main__':
    app.run(debug=True)
