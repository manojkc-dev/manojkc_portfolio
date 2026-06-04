# create_db.py
from database import engine, Base
import models  # This triggers the registration of the models

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done!")