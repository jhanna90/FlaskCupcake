from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="Vanilla",
    size="small",
    rating=3,
)

c2 = Cupcake(
    flavor="Peanut Butter Cup",
    size="large",
    rating=9,
    image="https://www.hersheyland.com/content/dam/hersheyland/en-us/recipes/recipe-images/450-reeses-peanut-butter-and-chocolate-cupcakes.jpeg",
)

db.session.add_all([c1, c2])
db.session.commit()
