from app import db


class OnePieceCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    crew = db.Column(db.String)
    devilFruit = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.name,
            "description": self.crew,
            "created_at": str(self.devilFruit)
        }