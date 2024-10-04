from flask import Flask, Response
import time
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Set this variable to control the wait time between steps
wait_time = 4  # in seconds, change this value as needed

# Dummy steps data with image URLs
steps = [
    {
        'id': 1,
        'description': 'Step 1: Uploading the environment image.',
        'imageUrl': 'https://picsum.photos/seed/step1/500/500'
    },
    {
        'id': 2,
        'description': 'Step 2: Segmenting the environment.',
        'imageUrl': 'https://picsum.photos/seed/picsum2/500/500'
    },
    {
        'id': 3,
        'description': 'Step 3: Analyzing textures.',
        'imageUrl': 'https://picsum.photos/seed/picsum3/500/500'
    },
    {
        'id': 4,
        'description': 'Step 4: Generating base noise.',
        'imageUrl': 'https://picsum.photos/seed/picsum4/500/500'
    },
    {
        'id': 5,
        'description': 'Step 5: Applying Voronoi tessellation.',
        'imageUrl': 'https://picsum.photos/seed/picsum5/500/500'
    },
    {
        'id': 6,
        'description': 'Step 6: Assigning textures to cells.',
        'imageUrl': 'https://picsum.photos/seed/picsum6/500/500'
    },
    {
        'id': 7,
        'description': 'Step 7: Blending textures.',
        'imageUrl': 'https://picsum.photos/seed/picsum7/500/500'
    },
    {
        'id': 8,
        'description': 'Step 8: Overlaying camouflage.',
        'imageUrl': 'https://picsum.photos/seed/picsum8/500/500'
    },
    {
        'id': 9,
        'description': 'Step 9: Object camouflage optimization.',
        'imageUrl': 'https://picsum.photos/seed/picsum9/500/500'
    },
    {
        'id': 10,
        'description': 'Step 10: Final camouflage generated.',
        'imageUrl': 'https://picsum.photos/seed/picsum10/500/500'
    }
]

# SSE route for streaming progress with image URLs
@app.route('/gencam', methods=['POST'])
def generate_camouflage():
    def event_stream():
        # Simulate processing steps with a delay
        for step in steps:
            time.sleep(wait_time)  # Wait before moving to the next step
            yield f'data: {{"id": {step["id"]}, "description": "{step["description"]}", "imageUrl": "{step["imageUrl"]}", "status": "completed"}}\n\n'
    
    # Return an SSE-compatible response
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
