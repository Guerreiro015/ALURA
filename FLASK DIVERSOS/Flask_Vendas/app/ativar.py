from flask import Flask, render_template, request, redirect, session,flash,send_from_directory
import mysql
from datetime import *
import time
import sqlite3
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pyodbc
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
#pip install PyMySQL

app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'


@app.route('/')
def salao():    

    return render_template('salao.html')


app.run(debug=True)

