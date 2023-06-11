import random
import string

from flask import Flask, render_template, request, redirect, url_for

from models import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

