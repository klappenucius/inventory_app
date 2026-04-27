from app import db
from datetime import db

#what do I need:

#Admin: first_name, last_name, email, password (will later be synced with Entra ID)
#User: first_name, last_name, email (will later be synced with Entra ID)
#Asset: with customizable fields: inventory_nr, name, model, manufacturer, serial_nr, cost, status,
    #default_loc, location, purchase_date, warranty_exipres, EOL, expected_return_date
#Accessory: name, model, manufacturer, serial_nr, cost, total_quantity, total_allocated,
    # each new batch can be created ny selecting "Add new batch" > what needs to be entered is purchase_date,
    # batch_quantity), batch_quantity, batch_assigned_qty, batch_available_qty, batch_purchase_date,
    # batch_assignees, warranty_expires, EOL, expected_return_date --> the idea is to enter a quantity and when
    # then allocate to users who were given this item if the quantity is >0
#Location

class Admin(db.Model):
    __tablename__="admins"

    id=db.Column(db.Integer, nullable=False, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False, )
    last_name=db.Column(db.String(50), nullable=False, )
    email=db.Column(db.String(30), nullable=False, unique=True)
    password=db.Column(db.String(15), nullable=False)

