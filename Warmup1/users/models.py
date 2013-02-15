from django.db import models
import json

# Create your models here.
SUCCESS               =   1  # : a success
ERR_BAD_CREDENTIALS   =  -1  # : (for login only) cannot find the user/password pair in the database
ERR_USER_EXISTS       =  -2  # : (for add only) trying to add a user that already exists
ERR_BAD_USERNAME      =  -3  # : (for add, or login) invalid user name (only empty string is invalid for now)
ERR_BAD_PASSWORD      =  -4


class UserManager(models.Manager):

        
#    @staticmethod                
    def login(self, userName, passWord):
        name = self.filter(username__exact = userName).exists()
        if (name == False):
            return ERR_BAD_CREDENTIALS
            #return -4
        else:
      #      account = Users.user_objects.get(username__exact = userName)
            account = self.get(username__exact = userName)
            if (passWord != account.password):
                return ERR_BAD_CREDENTIALS
            else:
                account.count = account.count + 1
                account.save()
           #     Users.save(account.username, account.password, account.count)
                return account.count

        
  #  @staticmethod
    def add(self, userName, passWord):
        name = self.filter(username__exact = userName).exists()
        if len(userName) == 0 or len(userName) > 128:
            return ERR_BAD_USERNAME
        elif len(passWord) > 128:
            return ERR_BAD_PASSWORD
        elif (name == True):
            return ERR_USER_EXISTS
        else:
            account = self.create(username = userName, password = passWord, count = 1)
            return account.count
            
    #@staticmethod        
    def resetFixture(self):
        self.all().delete()
        return SUCCESS
        
        
  #  @staticmethod                
    def unitTests(self):
        return SUCCESS    
        

class Users(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    count = models.IntegerField()
    user_objects = UserManager()
 
    #def save(self, *args, **kwargs):
    #    super(Users, self).save(*args, **kwargs) # Call the "real" save() method

