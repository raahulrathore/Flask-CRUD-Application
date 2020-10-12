# GDT1
This Task involve Dockerizing a Flask app which will help performing CRUD Operations upon the DataBase file which is being hosted at MongoDB's Atlas server.

Use the initial code.py to upload the JSON file which was being given to the mongo server.
GDuser indicate the username and password of the database. 

Then install docker on a system and run the dockerfile to build the image.

The port number is 5001 which can be accessed from 127.0.0.1:port_number 
5001 in this case so it'll be :
127.0.0.1:5001

The flask app is being built to Perform CRUD operations 
And the same can be verified using postman

The commands for performing CRUD operations on the database are
/getdata
/putdata
/update
/delete

and the same operations can be checked from the Screenshots 

The dependencies of the app are being given on Requirements.txt file and the same can be installed using pip3 install -r requirements.txt command in shell
