from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gear.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Модель для снаряжения
class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Gear {self.name}>"


# Создание базы данных
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    gear_list = Gear.query.all()
    return render_template("index.html", gear=gear_list)


@app.route("/add", methods=["POST"])
def add_gear():
    name = request.form.get("name")
    category = request.form.get("category")
    quantity = request.form.get("quantity")

    if name and category and quantity:
        new_gear = Gear(name=name, category=category, quantity=int(quantity))
        db.session.add(new_gear)
        db.session.commit()

    return redirect(url_for("home"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_gear(id):
    gear = Gear.query.get_or_404(id)
    db.session.delete(gear)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)