#%%

from sqlalchemy import create_engine


engine = create_engine("sqlite:///example-using-sql/twitter.db")

with engine.connect() as conn:
    results = conn.execute("select * from users")

    for r in results:
        print(r)
