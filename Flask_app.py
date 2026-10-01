from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="background-color: #e8f0fe; font-family: Arial; text-align: center; padding-top: 50px;">
        <div style="background-color: white; max-width: 400px; margin: auto; padding: 40px; border-radius: 16px;">
            <h1 style="color: #1a73e8; font-size: 36px;">MAXI</h1>
            <p style="color: #666; margin-bottom: 30px;">Welcome to your trusted platform</p>
            <a href="#" style="display: block; background-color: #1a73e8; color: white; padding: 14px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-bottom: 12px;">Create Account</a>
            <a href="#" style="display: block; background-color: white; color: #1a73e8; border: 2px solid #1a73e8; padding: 14px; border-radius: 8px; text-decoration: none; font-weight: bold;">Sign In</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
  
