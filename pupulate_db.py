from models import CarProject, db
from app import app
import datetime

with app.app_context():
    projects = [
        CarProject(manufacturer="Tesla", model="Model S", engine_size=0.0, power_output=670, price=79990.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Ford", model="Mustang GT", engine_size=5.0, power_output=450, price=55995.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Chevrolet", model="Camaro ZL1", engine_size=6.2, power_output=650, price=62995.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="BMW", model="M3", engine_size=3.0, power_output=473, price=70900.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Audi", model="RS5", engine_size=2.9, power_output=444, price=76000.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Mercedes-Benz", model="AMG C63", engine_size=4.0, power_output=503, price=69000.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Porsche", model="911 Carrera", engine_size=3.0, power_output=379, price=106100.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Lamborghini", model="Huracan EVO", engine_size=5.2, power_output=640, price=206485.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Ferrari", model="Roma", engine_size=3.9, power_output=612, price=222620.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Toyota", model="Supra GR", engine_size=3.0, power_output=382, price=54315.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Nissan", model="GT-R", engine_size=3.8, power_output=565, price=113540.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Hyundai", model="Ioniq 5", engine_size=0.0, power_output=320, price=45925.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Kia", model="EV6", engine_size=0.0, power_output=320, price=50500.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Volkswagen", model="Golf R", engine_size=2.0, power_output=315, price=44590.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Subaru", model="WRX STI", engine_size=2.5, power_output=310, price=37000.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Dodge", model="Challenger Hellcat", engine_size=6.2, power_output=717, price=61950.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Jeep", model="Grand Cherokee Trackhawk", engine_size=6.2, power_output=707, price=87395.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Mitsubishi", model="Lancer Evolution X", engine_size=2.0, power_output=291, price=38295.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Honda", model="Civic Type R", engine_size=2.0, power_output=315, price=43995.0, created_at=datetime.datetime.now()),
        CarProject(manufacturer="Mazda", model="MX-5 Miata", engine_size=2.0, power_output=181, price=28595.0, created_at=datetime.datetime.now()),
    ]

    db.session.add_all(projects)
    db.session.commit()
    print("Database populated with 20 car projects!")


