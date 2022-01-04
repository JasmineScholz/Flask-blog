from flask import Flask, jsonify, request
app=Flask(__name__)
#we are importing our function from the colors.py file
from colors import top_colors
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
#getting the url argument       
        url = request.args.get('url')
        result=top_colors(str(url))
        return jsonify(result)
    else:
        return jsonify({'Error':"This is a GET API method"})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9007)