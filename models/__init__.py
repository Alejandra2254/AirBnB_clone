#!/usr/bin/python3
"""updating with instance of FileStorage"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()