from flask import Flask, jsonify, request, abort 
import time  

def is_palindrome(my_string):
    lowercase_chars = ''.join(char for char in my_string if char.isalnum()).lower() #Punctuation including special characters are ignored. Numbers stay the same and all characters are changed to lowercase for effective comparison of content.
    if lowercase_chars==lowercase_chars[::-1]: #testing content of original and reversed string for equality.
        return True
    else: 
        return False    
    
app = Flask(__name__) 

palindromes = [] #initialising empty array of to-be palindromes, which will be dictionaries

@app.route('/palindrome', methods=['POST'])
def add_palindrome():
    if not request.json: #request object must have a json attribute given an input.
        abort(400)
    if type(request.json) != str: #user must input a string.
        abort(400)
    palindrome_content = request.json
    if is_palindrome(palindrome_content)==True: 
        new_palindrome = {
            "content": palindrome_content, 
            "time": time.time()
        } #palindrome content is stored in a dictionary along with the time it was initialised.
        palindromes.append(new_palindrome) 
    
        return jsonify(True) #output must be JSON so that it can be passed through to the client as output.
    else: 
        return jsonify(False) 
    

@app.route('/palindromes', methods=['GET'])
def get_palindromes():
    current_time = time.time(); 
    recent_palindromes = [palindrome for palindrome in palindromes if current_time-palindrome["time"]<=600] #taking those palindromes that are within the 10 min range of the current time. The default unit for time is seconds, hence conversion is used.
    palindromes_to_print = []; #initialising empty array of recent palindrome content, which are strings.
    for palindrome in recent_palindromes: 
        palindromes_to_print.append(palindrome["content"]) #only taking the content of the palindrome to print.
    most_recent_index = len(palindromes_to_print)-1
    return jsonify(palindromes_to_print[most_recent_index:most_recent_index-10:-1]) #taking the last ten most recent palindromes, from most recent to least recent in descending order. 

if __name__ == '__main__':
    app.run(debug=False,port =8080) # you can change debug to True if you would like to run it in debug mode. 