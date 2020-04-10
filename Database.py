import mysql.connector as mysql


def CreateConnection():
    connection = mysql.connect(host='localhost',
                                database='UserData',
                                user='root',
                                password='')
    return connection

def CreateTable():
    CreateDataBase()
    query = ("""CREATE TABLE IF NOT EXISTS Users
    (
        Id integer not null auto_increment,
        Name text not null,
        Email text not null,
        User text not null,
        Password text not null,
        Primary key (id)
    );

    """)

    ExecuteQuery(query)

    

def ExecuteQuery(query):
    connection = CreateConnection()
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    connection.commit()
    connection.close()


def CreateDataBase():
    connection = mysql.connect(host='localhost',
                                user='root',
                                password='')
    query = ("CREATE DATABASE IF NOT EXISTS UserData")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
   

def SelectUser(user,password):
    query = ("""SELECT user, password FROM users WHERE user=\'"""
    +user+"\' AND password=\'"+password+"\'")
    return query


def VerifyLogin(user,password):
    connection = CreateConnection()
    query = SelectUser(user,password)
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
   
    return cursor.fetchone()

