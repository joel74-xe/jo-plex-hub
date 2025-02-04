from flask import Flask, render_template
from flask_cors import CORS
CORS(app)
import subprocess

app = Flask(__name__)

# Function to get Plex server status (Windows)
def get_plex_server_status():
    try:
        # Check if Plex Media Server is running by using tasklist on Windows
        plex_status = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq Plex Media Server.exe'], capture_output=True, text=True)
        
        if 'Plex Media Server.exe' in plex_status.stdout:
            return "Plex server is running", "bg-green-500"
        else:
            return "Plex server is not running", "bg-red-500"
    except Exception as e:
        return f"Error checking status: {str(e)}", "bg-gray-500"

@app.route('/')
def index():
    plex_status, status_class = get_plex_server_status()
    return render_template('index.html', status=plex_status, status_class=status_class)

if __name__ == '__main__':
    app.run(debug=True)
