# Save this entire code into your mysite.py file in VS Code!
import os
import http.server
import socketserver

# HTML Content with smooth, modern design boxes for your portfolio biography
web_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gatbel's Personal Portfolio</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #10b981;
            --accent-hover: #059669;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            max-width: 800px;
            width: 100%;
        }

        /* Hero Header Section */
        header {
            text-align: center;
            margin-bottom: 40px;
        }

        h1 {
            color: var(--text-main);
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .subtitle {
            color: var(--accent);
            font-size: 1.2rem;
            font-weight: 500;
            margin-top: 0;
        }

        /* Smooth Card Container Grid */
        .bio-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 24px;
            margin-bottom: 40px;
        }

        @media (min-width: 640px) {
            .bio-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .full-width {
                grid-column: span 2;
            }
        }

        .card {
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .card:hover {
            transform: translateY(-2px);
            border-color: rgba(16, 185, 129, 0.3);
        }

        h2 {
            color: var(--text-main);
            font-size: 1.25rem;
            margin-top: 0;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        p {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.6;
            margin: 0;
        }

        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 12px;
        }

        .tag {
            background-color: rgba(16, 185, 129, 0.1);
            color: var(--accent);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        /* Action Interactive Button Area */
        .action-area {
            text-align: center;
        }

        .btn {
            background-color: var(--accent);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s ease;
        }

        .btn:hover {
            background-color: var(--accent-hover);
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>Gatbel Reath</h1>
            <p class="subtitle">Builder, Thinker & Alumnus Volunteer</p>
        </header>

        <main class="bio-grid">
            
            <!-- About Me Box -->
            <div class="card full-width">
                <h2>👤 About Me</h2>
                <p>Driven by resilience, creativity, and hard work, I focus on unlocking solutions through continuous learning. I dedicate my spare time to giving back to student programs and driving positive community impact in Addis Ababa.</p>
            </div>

            <!-- Academic Interests Box -->
            <div class="card">
                <h2>📚 Academic Passions</h2>
                <p>Deeply engaged in mathematics, philosophy, and critical thinking. I love diving into complex system puzzles, structural logic, and exploring future boundaries at the intersection of medicine and technology.</p>
                <div class="tag-container">
                    <span class="tag">Mathematics</span>
                    <span class="tag">Philosophy</span>
                    <span class="tag">Critical Thinking</span>
                </div>
            </div>

            <!-- Innovation & Projects Box -->
            <div class="card">
                <h2>💡 Innovation Projects</h2>
                <p>Always experimenting with creative engineering concepts. My hands-on projects range from investigating local water filtration systems to tinkering with robotics designs and web development pipelines.</p>
                <div class="tag-container">
                    <span class="tag">Web Backend</span>
                    <span class="tag">Robotics</span>
                    <span class="tag">Sustainability</span>
                </div>
            </div>

        </main>

        <div class="action-area">
            <button class="btn" onclick="alert('Network logic connected safely!')">Test Connection</button>
        </div>
    </div>

</body>
</html>
"""

# Force Python to create files locally in the project folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Write the index file securely
with open("index.html", "w") as file:
    file.write(web_content)

# Configure and fire up the web application host server
PORT = 10000
handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server... Access local port route: http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
