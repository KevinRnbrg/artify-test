from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/artify_database'
db = SQLAlchemy(app)
CORS(app)

def dfs(obj, objects, sorted_objects):
    sorted_objects.append(obj)
    children = [child for child in objects if child['parent'] == obj['id']]
    children.sort(key=lambda x: x['id'])
    for child in children:
        dfs(child, objects, sorted_objects)

def sort_objects_by_parent(objects):
    sorted_objects = []
    top_level_parents = [obj for obj in objects if obj['parent'] is None]
    top_level_parents.sort(key=lambda x: x['id'])
    for parent in top_level_parents:
        dfs(parent, objects, sorted_objects)
    return sorted_objects

class Sector(db.Model):
    __tablename__ = 'Sector'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    parentid = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent': self.parentid
        }
    
class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255))
    AgreeToTerms = db.Column(db.Boolean)
    sectors = db.relationship('Sector', secondary='UserSector', backref=db.backref('users', lazy='dynamic'))

UserSector = db.Table('UserSector',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.UserID')),
    db.Column('sector_id', db.Integer, db.ForeignKey('Sector.id'))
)

@app.route('/sectors')
def get_sectors():
    sectors = Sector.query.all()
    sector_list = [sector.to_dict() for sector in sectors]
    sorted_sector_list = sort_objects_by_parent(sector_list)
    return jsonify(sorted_sector_list)

@app.route('/create-tables')
def create_database_tables():
    try:
        db.create_all()
        return 'Database tables created successfully.'
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save-user', methods=['POST'])
def save_user_data():
    try:
        data = request.json
        name = data['name']
        sectors = data['sectors']
        agree_terms = bool(data['agree'])

        user = User(Name=name, AgreeToTerms=agree_terms)
        
        sector_instances = Sector.query.filter(Sector.id.in_(sectors)).all()
        for sector in sector_instances:
            user.sectors.append(sector)
        db.session.add(user)

        db.session.commit()
        user_id = user.UserID
        return jsonify({'user_id': user_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update-user', methods=['POST'])
def update_user_data():
    try:
        data = request.json
        user_id = int(data['user_id'])
        name = data['name']
        sectors = data['sectors']
        agree_terms = bool(data['agree'])

        user = User.query.get(user_id)

        if user:
            user.Name = name
            user.AgreeToTerms = agree_terms

            user.sectors = []
            sector_instances = Sector.query.filter(Sector.id.in_(sectors)).all()
            for sector in sector_instances:
                user.sectors.append(sector)

            db.session.commit()

            return jsonify({'message': 'User information updated successfully.'}), 200
        else:
            return jsonify({'error': 'User not found.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/populate-sector')
def populate_sector_table():
    try:
        manufacturing = Sector(name='Manufacturing', parentid=None)
        db.session.add(manufacturing)
        db.session.commit()

        other = Sector(name='Other', parentid=None)
        db.session.add(other)
        db.session.commit()

        service = Sector(name='Service', parentid=None)
        db.session.add(service)
        db.session.commit()

        manufacturing_id = manufacturing.id
        other_id = other.id
        service_id = service.id

        manufacturing_sectors = [
            Sector(name='Construction materials', parentid=manufacturing_id),
            Sector(name='Electronics and Optics', parentid=manufacturing_id),
            Sector(name='Food and Beverage', parentid=manufacturing_id),
            Sector(name='Furniture', parentid=manufacturing_id),
            Sector(name='Plastic and Rubber', parentid=manufacturing_id)
        ]

        other_sectors = [
            Sector(name='Creative industries', parentid=other_id),
            Sector(name='Energy technology', parentid=other_id),
            Sector(name='Environment', parentid=other_id)
        ]

        service_sectors = [
            Sector(name='Business services', parentid=service_id),
            Sector(name='Engineering', parentid=service_id),
            Sector(name='Information Technology and Telecommunications', parentid=service_id),
            Sector(name='Tourism', parentid=service_id),
            Sector(name='Translation services', parentid=service_id),
            Sector(name='Transport and Logistics', parentid=service_id)
        ]

        for sector in manufacturing_sectors + other_sectors + service_sectors:
            db.session.add(sector)
            db.session.commit()

        food_and_beverage_id = Sector.query.filter_by(name='Food and Beverage').first().id
        furniture_id = Sector.query.filter_by(name='Furniture').first().id
        plastic_and_rubber_id = Sector.query.filter_by(name='Plastic and Rubber').first().id
        it_telecom_id = Sector.query.filter_by(name='Information Technology and Telecommunications').first().id
        transport_logistics_id = Sector.query.filter_by(name='Transport and Logistics').first().id

        food_and_beverage_sectors = [
            Sector(name='Bakery & confectionery products', parentid=food_and_beverage_id),
            Sector(name='Beverages', parentid=food_and_beverage_id),
            Sector(name='Fish & fish products', parentid=food_and_beverage_id),
            Sector(name='Meat & meat products', parentid=food_and_beverage_id),
            Sector(name='Milk & dairy products', parentid=food_and_beverage_id),
            Sector(name='Other', parentid=food_and_beverage_id),
            Sector(name='Sweets & snack food', parentid=food_and_beverage_id)
        ]

        furniture_sectors = [
            Sector(name='Bathroom', parentid=furniture_id),
            Sector(name='Bedroom', parentid=furniture_id),
            Sector(name='Kitchen', parentid=furniture_id),
            Sector(name='Living room', parentid=furniture_id),
            Sector(name='Office', parentid=furniture_id),
            Sector(name='Other (Furniture)', parentid=furniture_id),
            Sector(name='Outdoor', parentid=furniture_id)
        ]

        plastic_and_rubber_sectors = [
            Sector(name='Packaging', parentid=plastic_and_rubber_id),
            Sector(name='Plastic processing technology', parentid=plastic_and_rubber_id),
            Sector(name='Plastic profiles', parentid=plastic_and_rubber_id)
        ]

        it_telecom_sectors = [
            Sector(name='Data processing, Web portals, E-marketing', parentid=it_telecom_id),
            Sector(name='Programming Consultancy', parentid=it_telecom_id),
            Sector(name='Software, Hardware', parentid=it_telecom_id)
        ]

        transport_logistics_sectors = [
            Sector(name='Air', parentid=transport_logistics_id),
            Sector(name='Rail', parentid=transport_logistics_id),
            Sector(name='Road', parentid=transport_logistics_id),
            Sector(name='Water', parentid=transport_logistics_id)
        ]

        for sector in food_and_beverage_sectors + furniture_sectors + plastic_and_rubber_sectors + it_telecom_sectors + transport_logistics_sectors:
            db.session.add(sector)
            db.session.commit()

        plastic_processing_technology_id = Sector.query.filter_by(name='Plastic processing technology').first().id

        plastic_processing_technology_sectors = [
            Sector(name='Blowing', parentid=plastic_processing_technology_id),
            Sector(name='Moulding', parentid=plastic_processing_technology_id),
            Sector(name='Plastics welding and processing', parentid=plastic_processing_technology_id),
        ]

        for sector in plastic_processing_technology_sectors:
            db.session.add(sector)
            db.session.commit()

        return 'Sector table populated successfully.'
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()

