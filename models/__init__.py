#!/usr/bin/python3
<<<<<<< HEAD
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
=======
"""FileStorage instance for application"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
>>>>>>> 6ecacbae983f5aabb6c9a32dec7a8687b856cd1f
storage.reload()
