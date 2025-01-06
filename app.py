from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

gear_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        quantity = request.form['quantity']

        gear_list.append({'name': name, 'category': category, 'quantity': quantity})

    return render_template('index.html', gear_list=gear_list)


@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    del gear_list[index]
    return redirect(url_for('index'))


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        gear_list[index]['name'] = request.form['name']
        gear_list[index]['category'] = request.form['category']
        gear_list[index]['quantity'] = request.form['quantity']
        return redirect(url_for('index'))

    item = gear_list[index]
    return render_template('edit.html', item=item, index=index)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
