from flask import Flask ## import Flask Class

AI=Flask(__name__) ## this is the name of the current module

@AI.route('/latha') ## url mapping
def latha():
    return 'Hello Good morning Everyone!!!!'
@AI.route('/joshi')
def joshi():
    return 'Had You Breakfast'

if __name__=='__main__':
    AI.run(debug=True,host='192.168.43.174',port=5002) ## run the server