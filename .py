from flask import Flask
import os

app = Flask(__name__)

@app.route("/render")
def render_scene():
    
    # blender command run
    os.system("blender -b -P main.py")
    
    return "Render complete! Check output folder."

if __name__ == "__main__":
    app.run(debug=True)
