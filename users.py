from db import db
from flask import session
from secrets import token_hex
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
            session["csrf_token"] = token_hex(16)
            return True
        else:
            return False

def logout():
    session.pop("user_id", None)  # Remove user_id key if exists
    session.pop("csrf_token", None)  # Remove csrf_token key if exists


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

def csrf_token():
    print(session.get("csrf_token", 0))
    return session.get("csrf_token", 0)

def user_name():
    user_id = session.get("user_id", 0)
    if user_id:
        sql = "SELECT username FROM Users WHERE id=:user_id"
        result = db.session.execute(text(sql), {"user_id":user_id})
        username = result.fetchone()
        if username:
            return username[0]
    return None

def is_admin():
    user_id = session.get("user_id", 0)
    if user_id:
        sql = "SELECT is_admin FROM Users WHERE id=:user_id"
        result = db.session.execute(text(sql), {"user_id":user_id})
        return result.fetchone()[0]
    else:
        return False
