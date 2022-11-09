from sqlalchemy import create_engine
import os

class FlatPostRepository:
    def __init__(self) -> None:
        db_name = os.getenv("POSTGRES_DB")
        db_user = os.getenv("POSTGRES_USER")
        db_pass = os.getenv("POSTGRES_PASSWORD")
        db_host = os.getenv("POSTGRES_DB_HOST")
        db_port = os.getenv("POSTGRES_DB_HOST")

        # Connecto to the database
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(
            db_user, db_pass, db_host, db_port, db_name)
        self.db = create_engine(db_string)
        
    def add_new_post(self, title, imageSrc):
        self.db.execute("INSERT INTO flatposts (title,imageurl) " +
                "VALUES (\'" +
                str(title) + "\',\'" +
                str(imageSrc) + "\');")
        
    def get_count(self):
        query = "" + \
            "SELECT COUNT(*) " + \
            "FROM flatposts "
            
        result = self.db.execute(query)
        
        return result
        
    def get_posts(self, num):
        
        results = []
        
        query = "" + \
            "SELECT * " + \
            "FROM flatposts " + \
            f"LIMIT {num}"

        result_set = self.db.execute(query)
        for r in result_set:
            results.append(r)
            
        return results
        

