Webcam Simulation: Local Recognition Test
📋 Overview
This simulation bypasses the physical IoT hardware (ESP32-CAM/PIR sensor) to test the facial recognition pipeline using your computer's webcam. It validates the "Application Unit" logic of the hybrid Edge-Cloud architecture. By running this test locally, you can determine optimal confidence thresholds and verify collection indexing without incurring hardware-related troubleshooting.

🛠️ Prerequisites
Before running the simulation, ensure your local environment is prepared:

Python 3.x: Installed on your machine.

Required Libraries:

Bash

pip install opencv-python boto3 awscli
opencv-python: For real-time video capture and frame manipulation.

boto3: The official AWS SDK for Python, used to communicate with Rekognition and S3.

awscli: The command-line interface for managing your AWS account services.

⚙️ Step 1: AWS Configuration
You must link your local machine to your AWS account. Open your terminal and run:

Bash

aws configure
Provide the following when prompted:

AWS Access Key ID: Found in your IAM console.

AWS Secret Access Key: Found in your IAM console.

Default region name: Use your preferred region (e.g., us-east-1).

Default output format: Type json (required for programmatic consistency).

📂 Step 2: Collection & Identity Indexing
AWS Rekognition uses "Collections" to store facial feature vectors.

Create the Collection:

Bash

aws rekognition create-collection --collection-id "authorized-users"
Index Your Identity: Save a clear selfie as me.jpg in your project folder and run the registration script (provided in previous steps). This creates the reference "ExternalImageId" that the system will search for.

🚀 Step 3: Running the Simulation
Execute the main recognition script:

Bash

python recognition_test.py
Controls:

SPACE: Capture a frame and send it to AWS for verification.

ESC: Exit the simulation.

Workflow Logic: The script performs a search_faces_by_image call, comparing the live frame to your "authorized-users" collection with a similarity threshold (recommended: 90%+).

🔬 Academic Justification
Edge-Cloud Trade-offs: This test mimics the "Cloud analytics" portion of a hybrid system, offloading complex stateful operations (face matching) to the Cloud to avoid the computational limitations of Edge devices.

Accuracy: While local LBP (Local Binary Pattern) algorithms typically achieve ~80% accuracy, this Cloud-based test utilizes deep learning models to achieve higher precision for intruder identification.

🛡️ Troubleshooting
"Collection Not Found": Ensure your terminal region matches the region where you ran create-collection.

Low Confidence: Improve lighting; Rekognition performs best when the face is clear and at a distance of less than 240 cm from the camera.
