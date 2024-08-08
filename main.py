from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    # Перенаправляем на страницу товара с id=1
    return redirect(url_for('product', product_id=1))

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    # Пример данных о товаре
    products = {
        1: {
            "title": "Товар 1",
            "description": "Подробное описание товара 1. Здесь вы можете узнать все подробности о нашем товаре, его характеристиках и преимуществах.",
            "image": "Снимок экрана 2024-08-08 в 05.53.14.png"
        },
        2: {
            "title": "Товар 2",
            "description": "Подробное описание товара 2. Этот товар отличается своими уникальными особенностями и характеристиками.",
            "image": "Снимок экрана 2024-08-08 в 05.55.04.png"
        }
    }
    product = products.get(product_id, {})
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)

