from flask import Flask,request,jsonify
#from flask_restful import Resource, Api, reqparse
from flask_restful import Api, Resource
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

#Variables para conexión a base de datos
pg_conn_data = {"host":os.getenv('HOST'),"user":os.getenv('USER'),"password":os.getenv('PASS'),"db":os.getenv('DB'),"port":os.getenv('PORT')}

import junglebranchs.dbpg