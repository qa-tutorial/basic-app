from application import db

class Names(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)

    def __repr__(self):
    	return ''.join([
            "Name ID: ", str(self.id), '\r\n',
            "Name: ", str(self.name), '\r\n', 
	])