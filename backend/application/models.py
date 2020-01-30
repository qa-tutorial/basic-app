from application import db

class Names(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    name_type = db.Column(db.String(10), nullable = False)

    def __repr__(self):
    	return ''.join([
            "Name ID: ", str(self.id), '\r\n',
            "Name: ", str(self.name), '\r\n', 
            "Name Type: ", str(self.name_type), '\r\n'
	])