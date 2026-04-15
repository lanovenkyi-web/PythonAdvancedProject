from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from HW_5 import engine, Base, Category, Question

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    db = get_db()
    try:
        new_cat = Category(name=data['name'], description=data.get('description'))
        db.add(new_cat)
        db.commit()
        db.refresh(new_cat)
        return {'id': new_cat.id, 'name': new_cat.name, 'description': new_cat.description}
    finally:
        db.close()

########################################################################################################################



@app.route('/categories', methods=['GET'])
def get_categories():
    db = get_db()
    try:
        cats = db.query(Category).all()
        return [{'id': c.id, 'name': c.name, 'description': c.description} for c in cats]
    finally:
        db.close()




#_______________________________________________________________________________________________________________________


@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    db = get_db()
    try:
        cat = db.query(Category).filter(Category.id == category_id).first()
        if not cat:
            return jsonify({'error': 'Category not found'}), 404

        cat.name = data.get('name', cat.name)
        cat.description = data.get('description', cat.description)
        db.commit()

        return {'id': cat.id, 'name': cat.name, 'description': cat.description}
    finally:
        db.close()





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    db = get_db()
    try:
        cat = db.query(Category).filter(Category.id == category_id).first()
        if not cat:
            return jsonify({'error': 'Category not found'}), 404

        db.delete(cat)
        db.commit()
        return {'message': 'Category deleted'}
    finally:
        db.close()




#=======================================================================================================================
@app.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()
    db = get_db()
    try:
        new_q = Question(
            text=data['text'],
            answer=data['answer'],
            category_id=data['category_id']
        )
        db.add(new_q)
        db.commit()
        db.refresh(new_q)
        return {
            'id': new_q.id,
            'text': new_q.text,
            'answer': new_q.answer,
            'category_id': new_q.category_id
        }
    finally:
        db.close()




#-----------------------------------------------------------------------------------------------------------------------
@app.route('/questions', methods=['GET'])
def get_questions():
    db = get_db()
    try:
        questions = db.query(Question).all()
        result = []
        for q in questions:
            result.append({
                'id': q.id,
                'text': q.text,
                'answer': q.answer,
                'category_id': q.category_id,
                'category': {
                    'id': q.category.id,
                    'name': q.category.name,
                    'description': q.category.description
                }
            })
        return result
    finally:
        db.close()




if __name__ == '__main__':
    app.run(debug=True)