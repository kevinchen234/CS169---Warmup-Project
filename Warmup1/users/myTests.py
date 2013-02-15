from users.models import Users, UserManager

#Test if database is cleared
    self.assertEquals(self.resetFixture(), 1)
#Test for logging in with user that's not in database
    self.assertEquals(self.login("add", "add"), -1)
    #Test for adding user not in database
    self.assertEquals(self.add("add", "add"), 1)
    #Test for adding user in database
    self.assertEquals(self.add("add", "add"), -2)
    #Test for logging in user in database
    self.assertEquals(self.login("add", "add"), 2)
    #Test for checking if count increases
    self.assertEquals(self.login("add", "add"), 3)
    #Test for logging in incorrectly
    self.assertEquals(self.login("add", "bcd"), -1)
    #Test for adding user with > 128 characters username
    self.assertEquals(self.add("CYtEuLuuutZjgQgxpeUZJUWTkOxSnSjMCpbqVlEJYHYdONIZibcTbLvRSTbRazIelzyMDMRciWJSLOXVUxiFnhmozWvQHBBFJgcYmvNeZROTSoLZQHeHYqIIzhwCdvyas", "asdfds"), -3)
    #Test for adding user with > 128 character password
    self.assertEquals(self.add("sdfsdfs", "CYtEuLuuutZjgQgxpeUZJUWTkOxSnSjMCpbqVlEJYHYdONIZibcTbLvRSTbRazIelzyMDMRciWJSLOXVUxiFnhmozWvQHBBFJgcYmvNeZROTSoLZQHeHYqIIzhwCdvyadfss"), -4)
    #Retest if database is cleared
    self.resetFixture()
    self.assertEquals(self.login("add", "add"), -1)

