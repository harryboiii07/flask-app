from flask import Flask
app = Flask(__name__)  # Fixed: Use __name__ instead of **name**

@app.route('/')
def hello():
    return "Hello from Flask running in a container!"  # Fixed: Indentation

if __name__ == "__main__":  # Fixed: Use __name__ and __main__ correctly
    app.run(host="0.0.0.0", port=5000)
