
from datetime import datetime
from database import db

class Tanka(db.Model):
  __tablename__ = 'tankas'

  id = db.Column(db.Integer, primary_key=True)

class TankaUnit(db.Model):
  __tablename__ = 'tanka_unit'

  text = db.Column(db.String(255), nullable=False)

  def to_dict():
    return {
      text: text
    }

class Favorite(db.Model):
  __tablename__ = 'favorite'

  timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)
