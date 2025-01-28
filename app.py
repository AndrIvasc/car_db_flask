"""
Full CRUD functionality
"""

from models import db, CarProject
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# fizines db prijungimas, configas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# paleidziam db
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("search_field")
    if search_text:
        filtered_row = CarProject.query.filter(CarProject.manufacturer.ilike(f"{search_text}"))
        return render_template("main_index.html", projects=filtered_row)
    else:
        all_projects = CarProject.query.all()
        return render_template("main_index.html", projects=all_projects)


@app.route("/car/<int:row_id>")
def one_project(row_id):
    project = CarProject.query.get(row_id)
    if project:
        return render_template("one_car_info.html", project=project)
    else:
        return f"The project with ID {row_id} does not exist."


@app.route("/car/edit/<int:row_id>", methods=["GET", "POST"])
def update_project(row_id):
    project = CarProject.query.get(row_id)
    if not project:
        return f"Project with ID {row_id} does not exist."

    if request.method == "GET":
        return render_template("update_car_info.html", project=project)

    elif request.method == "POST":
        manufacturer = request.form.get("manufacturer_field")
        model = request.form.get("model_field")
        engine_size = request.form.get("engine_size_field")
        power_output = request.form.get("power_output_field")
        price = request.form.get("price_field")

        if manufacturer:
            project.manufacturer = manufacturer
        if model:
            project.model = model
        if engine_size:
            project.engine_size = float(engine_size)
        if power_output:
            project.power_output = float(power_output)
        if price:
            project.price = float(price)

        db.session.commit()
        return redirect(url_for("home"))


@app.route("/car/delete/<int:row_id>", methods=["POST"])
def delete_project(row_id):
    project = CarProject.query.get(row_id)
    if not project:
        return f"Project with ID {row_id} does not exist."
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/car/new", methods=["GET", "POST"])
def create_project():
    if request.method == "GET":
        return render_template("create_car_form.html")
    elif request.method == "POST":
        manufacturer = request.form.get("manufacturer_field")
        model = request.form.get("model_field")
        engine_size = float(request.form.get("engine_size_field"))
        power_output = float(request.form.get("power_output_field"))
        price = float(request.form.get("price_field"))

        new_car = CarProject(
            manufacturer=manufacturer,
            model=model,
            engine_size=engine_size,
            power_output=power_output,
            price=price
        )
        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
