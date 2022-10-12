import pandas as pd
from .settings import db
def table_to_csv(query, path = "temp/result.csv"):
    df = pd.read_sql(query.statement, query.session.bind)
    df.to_csv(path)
    