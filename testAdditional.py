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
    
    
    
    
    
    
    
    
    
def testAddUserExists(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData2, errCode = -2)

def testAddUserExists(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData2, errCode = -2)

def testAddUserExists(self):
    respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
    self.assertResponse(respData2, errCode = -2)

