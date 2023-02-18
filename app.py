from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    Response,
    jsonify,
    make_response,
)
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/news"
db = SQLAlchemy(app)
ma = Marshmallow(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))
    is_delete = db.Column(db.Integer, default=0)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class Articles(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(200), nullable=False)
    published_date = db.Column(db.DateTime, server_default=db.func.now())
    updated_date = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    status = db.Column(db.Integer, default=1)
    is_delete = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(100))
    author = db.relationship("Users")
    category = db.relationship("Category")

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    url_link = db.Column(db.String(100))
    is_delete = db.Column(db.Integer, default=0)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class UsersSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Users
        sqla_session = db.session
        exclude = ("is_delete",)

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    # password = fields.String(required=True)
    role = fields.String(required=True)
    # is_delete = fields.Boolean(default =1)


class CategorySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Category
        sqla_session = db.session
        exclude = ("is_delete",)

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    is_delete = fields.Integer(required=True)
    url_link = fields.String(required=True)


class ArticleSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Articles
        include_fk = True
        sqla_session = db.session
        exclude = ("is_delete",)

    author = fields.Nested(UsersSchema)
    category = fields.Nested(CategorySchema)
    id = fields.Integer(dump_only=True)
    author_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)
    status = fields.Integer(required=True)
    image_url = fields.String(required=True)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    category_schema = UsersSchema()
    user = category_schema.load(data)
    result = category_schema.dump(user.create())
    return make_response(jsonify({"Message": "User created successfully"}), 200)


@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    user = Users.query.filter_by(email=email).first()
    users_schema = UsersSchema()
    if not user:
        return make_response(jsonify({'message': 'Email not found'}), 204)
    if user.password != password:
        return make_response(jsonify({'message': 'Incorrect password'}), 204)
    user = users_schema.dump(user)
    return make_response(jsonify({"Message": "Log in successfully", "data": user}), 200)


@app.route('/addCategory', methods=['POST'])
def addCategory():
    data = request.get_json()
    category_schema = CategorySchema()
    category = category_schema.load(data)
    result = category_schema.dump(category.create())
    return make_response(jsonify({"Message": "category created successfully"}), 200)


@app.route('/addArticle', methods=['POST'])
def addArticle():
    data = request.get_json()
    article_schema = ArticleSchema()
    article = article_schema.load(data)
    result = article_schema.dump(article.create())
    return make_response(jsonify({"Message": "article created successfully"}), 200)


@app.route('/getAllArticle', methods=['GET'])
def getAllArticle():
    getAllArticle = Articles.query.filter_by(is_delete=0).all()
    article_schema = ArticleSchema(many=True)
    articles = article_schema.dump(getAllArticle)
    return make_response(jsonify(articles), 200)


@app.route('/getAllCategories', methods=['GET'])
def getAllCategories():
    getAllCategories = Category.query.filter_by(is_delete=0).all()
    category_schema = CategorySchema(many=True)
    categories = category_schema.dump(getAllCategories)
    return make_response(jsonify(categories), 200)

@app.route('/getAllAdmin', methods=['GET'])
def getAllAdmin():
    getAllAdmin = Users.query.filter_by(role='admin').all()
    user_Schema = UsersSchema(many=True)
    admins = user_Schema.dump(getAllAdmin)
    return make_response(jsonify(admins), 200)


# @app.route('/getArticleById/<articleid>', methods=['GET'])
# def getArticleById(articleid):
#     getArticleById = Articles.query.get(articleid)
#     if not getArticleById:
#         return make_response(jsonify({'message': 'Article not found'}), 204)
#     else:
#         article_schema = ArticleSchema()
#         article = article_schema.dump(getArticleById)
#         return make_response(jsonify(article), 200)



@app.route('/getArticleById/<articleid>', methods=['GET'])
def getArticleById(articleid):
    if (Articles.query.get(articleid)):
        getArticleById = Articles.query.get(articleid)
        article_schema = ArticleSchema()
        article = article_schema.dump(getArticleById)
        return make_response(jsonify(article), 200)
    else:
        return make_response(jsonify({'message': 'Article not found'}), 204)


@app.route('/getArticleByCategory/<category>', methods=['GET'])
def getArticleByCategory(category):
    try:
        articles = Articles.query.join(Category).filter(Category.name == category, Articles.is_delete==0).all()
        article_schema = ArticleSchema(many=True)
        articles_json = article_schema.dump(articles)
        return make_response(jsonify(articles_json), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)



# @app.route('/getArticleByCategory/<category>', methods=['GET'])
# def getArticleByCategory(category):
#     getArticleByCategory = Articles.query.join(Category).filter(Category.name == category).filter_by(is_delete=0).all()
#     article_schema = ArticleSchema(many=True)
#     articles = article_schema.dump(getArticleByCategory)
#     return make_response(jsonify(articles), 200)
#

@app.route('/updateArticle/<id>', methods=['PUT'])
def updateArticle(id):
    if Articles.query.get(id):
        article=Articles.query.get(id)
        if(article.is_delete==1):
            return make_response(jsonify({"Message": "No Records Found"}), 204)
        else:
            data = request.get_json()
            article_schema = ArticleSchema()
            article = article_schema.load(data, instance=article)
            result = article_schema.dump(article.create())
            return make_response(jsonify({"Message": "Article updated successfully", "data": result}), 200)
    else:
        return make_response(jsonify({"Message": "No Records Found"}), 204)

    # article = Articles.query.filter_by(id=id, is_delete=0).first()
    # if not article:
    #     return make_response(jsonify({'message': 'Article not found',}), 204)
    #
    #
    # article_schema = ArticleSchema()
    # article = article_schema.load(data, instance=article)
    # result = article_schema.dump(article.create())
    #
    # return make_response(jsonify({"Message": "Article updated successfully", "data": result}), 200)



@app.route("/deleteArticle/<id>", methods=["DELETE"])
def deleteArticleById(id):
    if Articles.query.get(id):
        getArticleById=Articles.query.get(id)
        if(getArticleById.is_delete==1):
            return make_response(jsonify({"Message": "No Records Found"}), 204)
        else:
            getArticleById.is_delete = 1
            db.session.add(getArticleById)
            db.session.commit()
            return make_response(jsonify({"Message": "article DELETED successfully"}), 200)
    else:
        return make_response(jsonify({"Message": "No Records Found"}), 204)


if __name__ == "__main__":
    app.run(debug=True)