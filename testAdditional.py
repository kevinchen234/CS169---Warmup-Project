import unittest
import os
import testLib


def testAddUser(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData, count = 1)
    
def testLoginUser(self):
    respData1 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData3 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData3, count = 3)
    
def testAddUserExists(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData2, errCode = -2)
    
def testLoginBadCredentials(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password123'} )
    self.assertResponse(respData2, errCode = -1)
     
    
def testBadUsername(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData, errCode = -3)

def testBadPassword(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData, errCode = -4)

def testDatabaseCleared(self):
    respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {} )
    respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData2, errCode = -1)

