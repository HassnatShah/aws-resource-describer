# app/models.py

from app import db

class EC2Instance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instance_id = db.Column(db.String(64), unique=True, nullable=False)
    instance_type = db.Column(db.String(64))
    state = db.Column(db.String(64))
    private_ip = db.Column(db.String(64))
    public_ip = db.Column(db.String(64))
    subnet_id = db.Column(db.String(64))
    vpc_id = db.Column(db.String(64))
    tags = db.Column(db.JSON)
    # Add additional fields as necessary