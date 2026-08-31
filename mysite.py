import http.server
import socketserver
import webbrowser
import os

# Define the HTML template layout
web_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Gatbel's Python Web App</title>
    <style>
        body { font-family: Arial; background: #1e293b; color: white; text-align: center; padding: 50px; }
        .card { background: #334155; padding: 40px; border-radius: 12px; display: inline-block; box-shadow: 0 10px 15px rgba(0,0,0,0.3); }
        h1 { color: #38bdf8; }
        button { background: #10b981; color: white; border: none; padding: 12px 24px; border-radius: 6px; font-size: 16px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Gatbel's Python Powered Website</h1>
        <p>This complete website is being served directly using backend Python logic!</p>
        <button onclick="alert('Success! Python is hosting this live page.')">Test Connection</button>
    </div>
</body>
</html>
"""

# Force Python to create files on your Desktop to avoid Permission Errors
desktop_path = os.path.expanduser("~/Desktop")
os.chdir(desktop_path)

# Write the index file securely
with open("index.html", "w") as file:
    file.write(web_content)

# Configure and fire up the web application host server
PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server... Open your browser to http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
