from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)

class User:

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data ['email']
        self.password = data['password']
        self.created_at = data ['created_at']   
        self.updated_at = data ['updated_at']
        

    @classmethod
    def create(cls,data):

        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password

        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        
        return connectToMySQL(DB).query_db(query,data)


    @staticmethod
    def login_validation(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not User.EMAIL_REGEX.match(data['email']):
            flash("email rules not respected")
            is_valid= False
        if not user_in_db:
            is_valid= False
            flash("user does not exist")
        elif not bcrypt.check_password_hash(user_in_db.password , data['password']):
            is_valid = False
            flash("incorrect password")
        return is_valid

    @staticmethod
    def register_validation(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) < 3:
            is_valid = False
            flash("Full name must be longer than 3 characters.")
        if len(data['last_name']) < 3:
            is_valid = False
            flash("last name must be longer than 3 characters.")
        if not User.EMAIL_REGEX.match(data['email']):
            flash("email rules not respected")
            is_valid= False
        if len(data['password']) < 8:
            is_valid = False
            flash("password must have at least 8 characters.")
        if data['password'] != data['confirm_password']:
            flash("password must match.")
            is_valid = False
        if user_in_db:
            is_valid = False
            flash("this user already exists")
        return is_valid


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result =  connectToMySQL(DB).query_db(query,data)

        if result:
            return User(result[0])
        return False
