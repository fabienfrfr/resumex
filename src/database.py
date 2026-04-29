import lancedb
import pandas as pd

class DatabaseRepository:
    def __init__(self, db_path="./data"):
        self.db = lancedb.connect(db_path)
        self._initialize_tables()

    def _initialize_tables(self):
        """Initialise les tables si elles n'existent pas."""
        schemas = {
            "consultants": ["id", "name", "email", "role"],
            "skills": ["id", "name"],
            "consultant_skills": ["consultant_id", "skill_id", "level"],
            "projects": ["id", "client_name", "project_name", "start_date"],
            "staffing": ["consultant_id", "project_id", "role_on_project"]
        }
        
        for table_name, columns in schemas.items():
            if table_name not in self.db.table_names():
                # Création d'un DF vide avec les bonnes colonnes
                df = pd.DataFrame(columns=columns)
                self.db.create_table(table_name, data=df)

    def get_dataframe(self, table_name):
        return self.db.open_table(table_name).to_pandas()

    def update_table(self, table_name, df):
        # On remplace la table par le nouveau DataFrame édité
        self.db.drop_table(table_name)
        self.db.create_table(table_name, data=df)