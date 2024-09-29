import os
from flask import Flask, abort, jsonify, request, Response, send_file
import time

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Define the directory where your images are stored
IMAGE_DIRECTORY = 'static/images/patterns'

@app.route('/download-image/<filename>', methods=['GET'])
def download_image(filename):
    try:
        # Build the full path to the file
        file_path = os.path.join(IMAGE_DIRECTORY, filename)

        # Check if the file exists
        if os.path.exists(file_path):
            # Send the file with the proper Content-Disposition header to trigger download
            return send_file(file_path, as_attachment=True, download_name=filename)
        else:
            abort(404)  # Return a 404 if the file is not found

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return error message if something goes wrong


@app.route('/progress', methods=['POST'])
def progress():
    # Check if the request contains images
    if 'images' not in request.files:
        return Response("No images part in the request", status=400)

    files = request.files.getlist('images')

    # Generator function to stream progress
    def generate():
        try:
            # Step 1: Image Uploading
            yield f"data: Step 1: Images Uploaded \n\n"
            time.sleep(1)  # Simulate the delay for processing

            # Step 2: Image Preprocessing
            yield f"data: Step 2: Image Preprocessing\n\n"
            time.sleep(1)

            # Step 3: Applying Filters
            yield f"data: Step 3: Applying Filters\n\n"
            time.sleep(1)

            # Step 4: Generating Camouflage
            yield f"data: Step 4: Generating Camouflage\n\n"
            time.sleep(1)

            # Step 5: Finishing
            yield f"data: Step 5: Finishing\n\n"
            time.sleep(1)

            # Once processing is done, send the final image URL
            image_url = "http://backend.intelilab.click/static/images/patterns/camouflaged_20240929010354.png"
            yield f"data: Image processed. View at {image_url}\n\n"
        
        except Exception as e:
            yield f"data: Error occurred: {str(e)}\n\n"

    # Return the event-stream response
    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
