import lancedb
import pandas as pd

class DatabaseRepository:
    def __init__(self, db_path="./ma_db", table_name="ma_table"):
        self.db = lancedb.connect(db_path)
        self.table_name = table_name
        self._ensure_table_exists()

    def _ensure_table_exists(self):
        try:
            self.table = self.db.open_table(self.table_name)
        except:
            initial_df = pd.DataFrame({"id": [1], "value": ["test"]})
            self.table = self.db.create_table(self.table_name, data=initial_df)

    def get_dataframe(self):
        return self.table.to_pandas()

    def update_table(self, df):
        self.table.overwrite(df)