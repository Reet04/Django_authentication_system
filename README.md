To access the authentication system of the project->
Go to newsite->authentication

All the dependencies(libraries) are present in requirement.txt

Functionalities->
  
  To get json file of all users->    
    http://127.0.0.1:8000/getjsonall
  
  To get json file of of a particular user->    
    http://127.0.0.1:8000/getjson/<id>/
    
  To print all the users in table format->
    http://127.0.0.1:8000/listall
  
  To print a particular user in table format->
    Method 1: http://127.0.0.1:8000/list/5/
    Method 2: http://127.0.0.1:8000/listget/?is_staff=False     (Using params)
  
 
