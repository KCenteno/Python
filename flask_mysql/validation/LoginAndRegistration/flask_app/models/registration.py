from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re
from flask_app import LR



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')


class Registration:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def save(cls, data):
        data = {
            "first_name" : data["first_name"],
            "last_name" : data["last_name"],
            "email" : data["email"],
            "password" : data["password"]
        }
        data["password"] = bcrypt.generate_password_hash(data["password"])
        query = "INSERT INTO registers ( first_name, last_name, email, password, created_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        return connectToMySQL(LR).query_db( query, data )


    @classmethod
    def with_email(cls, data):
        query = "SELECT * FROM registers WHERE email = %(email)s"
        results = connectToMySQL(LR).query_db(query, data)
        if results:
            return cls(results[0])
        return False


    # @classmethod
    # def select_id(cls, **data):
    #     query = "SELECT * FROM registers WHERE id = %(id)s"
    #     results = connectToMySQL(LR).query_db(query, data)
    #     return cls(results[0])


    @classmethod
    def check_login(cls, data):
        in_db = Registration.with_email(data)
        if not in_db:
            flash("invalid Email/Password", 'log')
            return False
        if not bcrypt.check_password_hash(in_db.password, data['password']):
            flash("invalid Email/Password", 'log')
            return False
        return True


    @staticmethod
    def validate_registers(registers):
        is_valid = True
        if len(registers['first_name']) < 2 or not NAME_REGEX.match( registers['first_name']):
            flash("First Name must be at least 2 characters.", 'reg')
            is_valid = False
        if len(registers['last_name']) < 2 or not NAME_REGEX.match( registers['last_name']):
            flash("Last Name must be at least 2 characters.", 'reg')
            is_valid = False
        query = "SELECT * FROM registers WHERE email = %(email)s;"
        results = connectToMySQL(LR).query_db(query, registers)
        if len(results) >= 1:
            flash("Email already taken.", 'reg')
            is_valid = False
        if not EMAIL_REGEX.match( registers['email']):
            flash("Email is not valid!", 'reg')
            is_valid = False
        if len(registers['password']) < 8:
            flash("Password needs to be longer.", 'reg')
            is_valid = False
        if (registers['cpassword']) != (registers['password']):
            flash("Passwords doesnt match.", 'reg')
            is_valid = False
        return is_valid