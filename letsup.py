from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)
@app.route('/')
def index():
   return render_template("index.html")
 

@app.route('/text', methods=['GET', 'POST'])
def text(comments=[]):
    if request.method == "GET":
        return render_template("index.html", comments=comments)    
    comments.append(request.form["text_input"]) 

    response = requests.put(
        'https://qui-demo.populiweb.com/api2/people/25', 
        headers={
            'Authorization': 'Bearer sk_2u6kmQB3tBeP2wQyuOgsbPgw5axXeN5b1roq3mq8DKmsVuxc7F8GjUBTEoLyehIz4XdFgPhKafMUQJZiKjgFPS'
  
        },
        json={
             'bio' : request.form["text_input"]
     

            }
 
 
        )

    
    

   
    return redirect(url_for('text'))










 
if __name__ == '__main__':
   app.run(debug=True)
   

