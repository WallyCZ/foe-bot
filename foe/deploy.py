
"""
"""

# Native
import random
import time

# 3rd-Party

# Proprietary
from . import db

session = db.session

db.drop()
print("Deploy: Dropped database")

db.init()
print("Deploy: Initialized database")

start = time.time()

print("Deploy: Committing to database...")

session.commit()

print("Deploy: Committed to database in %.2fs" % (time.time() - start))
