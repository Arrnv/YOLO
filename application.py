from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from src.main import main 

application= Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output_videos'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
ALLOWED_EXTENSIONS = {'mp4'}

# Ensure upload and output folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/process', methods=['POST'])
def process_video():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
        output_path = os.path.join(application.config['OUTPUT_FOLDER'], 'output_video.mp4')

        # Save the file to the upload folder
        file.save(input_path)

        # Call the main function of your script
        try:
            main(input_path, output_path)  # Modify main() to accept input/output paths
        except Exception as e:
            return f"Error processing video: {e}", 500

        return redirect(url_for('download_video'))

    return "Invalid file type", 400

@application.route('/download')
def download_video():
    return render_template('download.html', video_path='/output_videos/output_video.avi')

if __name__ == '__main__':
    application.run(debug=True)
