# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from users.models import Users, UserManager
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt


import json


SUCCESS               =   1  # : a success
ERR_BAD_CREDENTIALS   =  -1  # : (for login only) cannot find the user/password pair in the database
ERR_USER_EXISTS       =  -2  # : (for add only) trying to add a user that already exists
ERR_BAD_USERNAME      =  -3  # : (for add, or login) invalid user name (only empty string is invalid for now)
ERR_BAD_PASSWORD      =  -4

@csrf_exempt        
def index(request):
    return render_to_response('client.html')

@csrf_exempt        
def login(request):
    infoRequest = json.loads(request.body)
    userName = infoRequest["user"]
    passWord = infoRequest["password"]
#    response = Users.login(userName, passWord)
    response = Users.user_objects.login(userName, passWord)
  #  response.save()
    if (response > 0):
      #  name = Users.user_objects.get(username__exact=userName)
        return HttpResponse(json.dumps({"errCode" : SUCCESS, "count" : response}), content_type = "application/json")
    elif (response < 0):
        return HttpResponse(json.dumps({"errCode" : -1}), content_type = "application/json") 

@csrf_exempt        
def add(request):
    infoRequest = json.loads(request.body)
   # infoRequest = json.loads("12321")
    userName = infoRequest["user"]
    passWord = infoRequest["password"]
#    response = Users.objects.add(userName, passWord)
    response = Users.user_objects.add(userName, passWord)
#    response = Users.add(userName, passWord)
#    response.save()
    if (response > 0):
      #  name = Users.user_objects.get(username__exact=userName)
        return HttpResponse(json.dumps({"errCode" : SUCCESS, "count" : response}), content_type = "application/json")
    elif (response == -4):
        return HttpResponse(json.dumps({"errCode" : -4}), content_type = "application/json") 
    elif (response == -3):
        return HttpResponse(json.dumps({"errCode" : -3}), content_type = "application/json") 
    elif (response == -2):
        return HttpResponse(json.dumps({"errCode" : -2}), content_type = "application/json")
        
        
@csrf_exempt        
def resetFixture(request):
 #   c = {}
#    c.update(csrf(request))
#    response = Users.resetFixture()
    response = Users.user_objects.resetFixture()
    if (response == SUCCESS):
        return HttpResponse(json.dumps({"errCode" : SUCCESS}), content_type = "application/json")

@csrf_exempt        
def unitTests(request):
    infoRequest = json.loads(request.body)
    buffer = StringIO.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(self.unitTests)
    result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)
#    response = Users.unitTests()

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
    


    rv = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
    return HttpResponse(json.dumps(rv), content_type = "application/json")
