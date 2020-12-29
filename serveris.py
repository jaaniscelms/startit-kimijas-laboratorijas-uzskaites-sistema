from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return "Labrīts!"

@app.route('/sveiki')
def sveiki():
  return "Nav vairs nekāds rīts!"

@app.route('/sveiki/<vards>')
def sveiki_vards(vards):
  return f"Sveiki, {vards}"

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)