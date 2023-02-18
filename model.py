# from flask_sqlalchemy import SQLAlchemy
# from marshmallow import fields
# from marshmallow_sqlalchemy import ModelSchema
# import app


# db = app.db

# class UsersSchema(ModelSchema):
#     class Meta(ModelSchema.Meta):
#         model = Users
#         sqla_session = db.session

#     id = fields.Number(dump_only=True)
#     name = fields.String(required=True)
#     email = fields.String(required=True)
#     password = fields.String(required=True)
#     role = fields.String(required=True)

