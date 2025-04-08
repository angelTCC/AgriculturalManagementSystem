from flask import Flask
from routes.crops import crops_bp

app = Flask(__name__)
app.register_blueprint(crops_bp)

if __name__=="__main__":
    app.run(debug=True)