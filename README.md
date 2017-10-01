# Palindromes
A simple RESTful API/service that stores valid palindromes that are entered by the user and returns the 10 most recent ones. 

This service is built in Python 3.6, using the Flask (0.12.2) web framework.

### Run instructions (Main application):
1. The best way to run an application that uses Flask is using a virtual environment. This can be set up using any environment
management package, my preference is either ['virtualenv'](https://pypi.python.org/pypi/virtualenv) or ['conda env'](https://conda.io/docs/user-guide/tasks/manage-environments.html)
,which is through Anaconda. It is possible to install Flask on the system and not in an environment, but is not recommended by its creators.
2. Once the environment is set up and activated, install Flask in this environment, my preference is using ['pip'.](https://docs.python.org/3/installing/index.html)
3. Now you can clone this repo in your chosen folder / directory or make a new one. 
4. When you're in this directory, run the 'palindromes.py' file. My preference is to run it using the 'python palindromes.py' command on command line. 
5. The app should be now running, you can choose to run it in debug mode if you want (see line 45 in palindromes.py). 

The local server link is: http://127.0.0.1:8080/
You can use any browser for the GET request (default request for browser), but for the post request, it is recommended to use a toolkit like ['Postman'](https://www.getpostman.com).

7. Using Postman or your tool of choice, write your candidate palindromes enclosed in quotation marks like any standard string. An example is: "Test Palindrome". Send this in your POST request. The service will
only accept strings.
8. Use the GET request to view the recent palindromes.

### Run instructions (Tests):
1. The test file is written using unittest, which is a module in Python. One can simply run all the tests by running the 
'test_palindromes.py' file, again my preference is to use the command line. 

### Notes: 
* There are comments in the code that guide you through how it works.
* The database for this service is using inbuilt data structures i.e. lists and dictionaries in Python. For more demanding and larger requirements, we could adapt the existing application to use SQL. 
* The main functions in pallindromes.py have been slightly amended for the test file in terms of what they retrieve and return, however the underlying logic is the same. 

### Comments / Potential Additions: 
Comments and potential additions have been written in the "Comments.txt" file.





