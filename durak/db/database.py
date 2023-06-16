from pony.orm import Database
from pony.orm import db_session

# Database singleton
db = Database()

session = db_session