from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class CarProject(db.Model):
    __tablename__ = "projektas"
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    engine_size = db.Column(db.Float, nullable=False)
    power_output = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def kaina_su_pvm(self):
        return round(self.price * 1.21, 2)

    @property
    def horse_power(self):
        return round(self.power_output * 1.341, 2)

    def __repr__(self):
        return (f"ID: {self.id}, Manufacturer: {self.manufacturer}, Model: {self.model}, "
                f"Engine Size: {self.engine_size}L, Power Output: {self.power_output}kW "
                f"({self.horse_power} HP), Price: {self.price} EUR, "
                f"Price with VAT: {self.kaina_su_pvm} EUR, Created At: {self.created_at}")
