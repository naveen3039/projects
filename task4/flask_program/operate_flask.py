from operati import *
from flask import Flask,request


app=Flask(__name__)


@app.route('/<operate>/<int:a>/<int:b>')
def cal(operate,a,b):
    call=Operations(a,b) 
    if operate == '+':
        c=call.add(a,b)
        return c
    if operate == '-':
        c=call.sub(a,b)
        return {'sub':str(c)}
    if operate == '*':
        c=call.mul(a,b)
        return {'mul':str(c)}
    if operate == 'div':
        c=call.div(a,b)
        return {'div':str(c)} 


@app.route('/')  
def home():
    return 'provide operator in symbol (+,-,*,div) and two values'


if __name__=='__main__':
    app.run(port=5006,debug=True) 


        