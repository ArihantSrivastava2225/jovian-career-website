from flask import Flask

app = Flask(__name__) #created a flask application

# now we need to tell flask what it should return when a certain url is requested. Hence we also need to register routes which are part of the url after the domain names
@app.route("/")
def hello_world():
    return "<p>Hello, World wow!</p>"

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  #we give debug = true so that everytime we make a change in the code, it automatically reloads the page