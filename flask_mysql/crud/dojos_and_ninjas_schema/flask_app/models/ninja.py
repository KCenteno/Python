from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojo_id = data["dojo_id"]

    @classmethod
    def all_ninjas(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas

    @classmethod
    def one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def pick_one(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(id)s"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas


    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), %(dojo_id)s);"
        new_id = connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)
        return new_id