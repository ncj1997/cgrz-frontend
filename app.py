from flask import Flask, request, Response
import time

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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
            time.sleep(2)  # Simulate the delay for processing

            # Step 2: Image Preprocessing
            yield f"data: Step 2: Image Preprocessing\n\n"
            time.sleep(2)

            # Step 3: Applying Filters
            yield f"data: Step 3: Applying Filters\n\n"
            time.sleep(2)

            # Step 4: Generating Camouflage
            yield f"data: Step 4: Generating Camouflage\n\n"
            time.sleep(2)

            # Step 5: Finishing
            yield f"data: Step 5: Finishing\n\n"
            time.sleep(2)

            # Once processing is done, send the final image URL
            image_url = "http://backend.intelilab.click/static/images/patterns/camouflaged_20240929010354.png"
            yield f"data: Image processed. View at {image_url}\n\n"
        
        except Exception as e:
            yield f"data: Error occurred: {str(e)}\n\n"

    # Return the event-stream response
    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
