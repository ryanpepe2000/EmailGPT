from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Recipient {self.email}>'

class EmailTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipient.id'), nullable=False)
    recipient = db.relationship('Recipient', backref=db.backref('emails', lazy=True))

    def __repr__(self):
        return f'<EmailTemplate for {self.recipient.email}>'