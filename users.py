from db import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password_hash FROM Users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO Users (username, password_hash, is_admin) VALUES (:username, :password, :admin)"
        db.session.execute(text(sql), {"username":username, "password":hash_value, "admin":False})
        db.session.commit()
    except:
        return False
    return login(username, password)
        
def user_id():
    return session.get("user_id", 0)

def user_name():
    user_id = session.get("user_id", 0)
    if user_id:
        sql = "SELECT username FROM Users WHERE id=:user_id"
        result = db.session.execute(text(sql), {"user_id":user_id})
        username = result.fetchone()
        if username:
            return username[0]
    return None
