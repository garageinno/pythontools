#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:46:56 2018
@author     : Sourabh
"""

# %%

from .AbstractDBM import AbstractDBM
from .DatabaseType import DatabaseType
from .SqliteDBM import SqliteDBM

class DatabaseManager(AbstractDBM):
    
    def __init__(self, dbtype=DatabaseType.default):
        self.__dbType = dbtype
        self.__dbm = self.__initDBM(dbtype)
    
    def __initDBM(self, dbtype):
        if dbtype == DatabaseType.sqlite:
            return SqliteDBM()
    
    def connectDB(self, dbpath):
        self.__dbm.connectDB(dbpath)
    
    def closeDB(self):
        self.__dbm.closeDB()
    
    def createTable(self, name, schema):
        self.__dbm.createTable(name, schema)
    
    def deleteTable(self, name):
        self.__dbm.deleteTable(name)
    
    def insertIntoTable(self, name, records):
        self.__dbm.insertIntoTable(name, records)
    
    def fetchAllFromTable(self, name):
        return self.__dbm.fetchAllFromTable(name)
    
    def saveTable(self, name):
        self.__dbm.saveTable(name)
    
    def executeQuery(self, query, records=None):
        return self.__dbm.executeQuery(query, records)
    
    def fetchOne(self):
        return self.__dbm.fetchOne()
    
    def fetchAll(self):
        return self.__dbm.fetchAll()
