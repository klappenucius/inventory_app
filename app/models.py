from app import db
from datetime import db

#what do I need:

# + Admin: first_name, last_name, email, password (will later be synced with Entra ID)
# + User: first_name, last_name, email (will later be synced with Entra ID)
# + Asset: with customizable fields: inventory_nr, name, model, manufacturer, serial_nr, cost, status,
    #default_loc, location, purchase_date, warranty_exipres, EOL, expected_return_date
# + Accessory: name, model, manufacturer, serial_nr, cost, total_quantity, total_allocated,
    # each new batch can be created ny selecting "Add new batch" > what needs to be entered is purchase_date,
    # batch_quantity), batch_quantity, batch_assigned_qty, batch_available_qty, batch_purchase_date,
    # batch_assignees, warranty_expires, EOL, expected_return_date --> the idea is to enter a quantity and when
    # then allocate to users who were given this item if the quantity is >0
# + Location
# + Manufacturer
# + Supplier
# + Model
#AccessoryBatch
# + Address
# + ContactPerson

class Admin(db.Model):
    __tablename__="admins"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False, )
    last_name=db.Column(db.String(100), nullable=False, )
    email=db.Column(db.String(70), nullable=False, unique=True)
    password=db.Column(db.String(15), nullable=False)

class User(db.Model):
    __tablename__-="users"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(70), nullable=False, unique=True)
    password=db.Column(db.String(15), nullable=False)

class Asset(db.Model):
    __tablename__="assets"
 
    id=db.Column(db.Integer, nullable=False, primary_key=True)
    inventory_nr=db.Column(db.Integer, nullable=False, unique=True)
    name=db.Column(db.String(50), nullable=False)
    serial_nr=db.Column(db.Integer, nullable=False, unique=True)
    cost=db.Column(db.Numeric(precision=10, scale=2), nullable=False) #for financial data; equivalent to Decimal in Java
    status=db.Column(db.String(30), nullable=False)
    default_loc=db.Column(db.String(100), nullable=False)
    location=db.Column(db.String(100), nullable=False)
    purchase_date=db.Column(db.Date, nullable=False)
    warranty_expires=db.Column(db.Date)
    eol=db.Column(db.Date)
    expected_return_date=db.Column(db.Date)

    model_id=db.Column(db.Integer, db.ForeignKey(models.id), nullable=False)
    supplier_id=db.Column(db.Integer, db.ForeignKey(suppliers.id), nullable=False)


class Accessory(db.Model):
    __tablename__="accessories"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    serial_nr=db.Column(db.Integer, nullable=False, unique=True)
    cost=db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    warranty_expires=db.Column(db.Date)
    eol=db.Column(db.Date)
    expected_return_date=db.Column(db.Date)

    model_id=db.Column(db.Integer, db.ForeignKey("models.id"))
    supplier_id=db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    batch_id=db.Column(db.Integer, db.ForeignKey("batches.id"))

class Location(db.Model):
    __tablename__="locations"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    name=db.Column(db.String(100), nullable=False)

class Manufacturer(db.Model):
    __tablename__="manufacturers"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    oib=db.Column(db.String(11), nullable=False, unique=True)
    name=db.Column(db.String(100), nullable=False)

    models=db.Relationship("Model", backref="manufacturer")

    address_id=db.Column(db.Integer, db.ForeignKey("addresses.id"))
    contactPerson_id=db.Column(db.Integer, db.ForeignKey("contactPeople.id"))

class Supplier(db.Model):
    __tablename__="suppliers"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    oib=db.Column(db.String(11), nullable=False, unique=True)
    name=db.Column(db.String(100), nullable=False)

    assets=db.Relationship("Asset", backref="supplier")
    accessories=db.Relationship("Accessory", backref="supplier")

    address_id=db.Column(db.Integer, db.ForeignKey("addresses.id"))
    contactPerson_id=db.Column(db.Integer, db.ForeignKey("contactPeople.id"))

class Model(db.Model):
    __tablename__="models"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    name=db.Column(db.String(100), nullable=False)

    manufacturer_id=db.Column(db.Integer, db.ForeignKey("manufacturers.id"), nullable=False)

class Address(db.Model):
    __tablename__="addresses"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    street=db.Column(db.String(100), nullable=False)
    house_nr=db.Column(db.Integer, nullable=False)
    postal_code=db.Column(db.Integer, nullable=False)
    city=db.Column(db.String(100), nullable=False)
    country=db.Column(db.String(100), nullable=False)

    manufacturers=db.Relationship("Manufacturer", backref="address")
    suppliers=db.Relationship("Supplier", backref="address")

class ContactPerson(db.Model):
    __tablename__="contactPeople"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False, )
    last_name=db.Column(db.String(100), nullable=False, )
    email=db.Column(db.String(70), nullable=False, unique=True)
    phone_nr=db.Column(db.integer)

    manufacturers=db.Relationship("Manufacturer", backref="contactPerson")
    suppliers=db.Relationship("Supplier", backref="contactPerson")


    # bach new batch can be created ny selecting "Add new batch" > what needs to be entered is purchase_date,
    # batch_quantity), batch_quantity, batch_assigned_qty, batch_available_qty, batch_purchase_date,
    # batch_assignees

class AccessoryBatch(db.Model):
    __tablename__="accessoryBatch"

    id=db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name=db.Column(db.integer, nullable=False, autoincrement=True)
    purchase_date=db.Column(db.Date, nullable=False)
    total_quantity=db.Column(db.Integer, nullable=False)
    assigned_quantity=db.Column(db.integer, nullable=False)
    available_quantity=db.Column(db.Integer, nullable=False)

    accessories=db.Relationship("Accessory", backref="batch")
