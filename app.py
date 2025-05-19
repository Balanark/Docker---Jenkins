from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask DevOps Demo</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 10px;
                display: inline-block;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.3em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask CI/CD Demo</h1>
            <p>Jenkins + Docker + AWS EC2!</p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
