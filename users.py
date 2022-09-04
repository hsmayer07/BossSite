import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from db import get_db
from hashlib import blake2b

class User():
    def __init__(self, name, uuid, email, pfp, hours, activities):
    	self.name = name;
    	self.uuid = uuid;
    	self.email = email;
    	self.pfp = pfp;
    	self.hours = hours;
    	self.activities = activities;

    @staticmethod
    def get_user_by_name(name):
        db = get_db();
        user = db.execute("SELECT * FROM user WHERE name = ?", (name));
        if not user:
            return None;
        return User(name = user[1], uuid = user[0], email = user[2], pfp = user[3], hours = user[4], activities = users[5]);

    @staticmethod
    def update_user(user):
    	db = get_db();
    	db.execute("UPDATE user SET uuid = ?, name = ?, email = ?, profile_pic  = ?, hours = ?, activites = ? WHERE uuid = ?", user.uuid, user.name, user.email, user,pfp, user.hours, user.activities);
    	db.commit();

    @staticmethod
    def create_user(name, email, pfp):
        db = get_db();
        uuid = blake2b(name).hexdigest()
        db.execute("INSERT INTO user (uuid, name, email, profile_pic, hours, activities) VALUES (0, ?, ?, ?, 0, NONE)", name, email, pfp)
        db.commit();
