from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW())"
        new_dojo = connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)
        return new_dojo
