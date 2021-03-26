from flask import render_template, url_for, request, redirect, session, flash
from app import app

@app.route('/')
def index():
    return render_template('index.html')