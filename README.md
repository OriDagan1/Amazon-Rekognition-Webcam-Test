
# Webcam Simulation: Local Recognition Test 🎥

## 📋 Overview

This simulation bypasses the physical IoT hardware (ESP32-CAM/PIR sensor) to test the facial recognition pipeline using your computer's webcam. It validates the "Application Unit" logic of the hybrid Edge-Cloud architecture. By running this test locally, you can determine optimal confidence thresholds and verify collection indexing without incurring hardware-related troubleshooting.

## 🛠️ Prerequisites

### Before running the simulation, ensure your local environment is prepared:

Python 3.x: Installed on your machine.

AWS Account: With permissions for Amazon Rekognition.


 Run the following command in your terminal to install the necessary Python packages:
 ```bash
 pip install opencv-python boto3 awscli
 ```
* opencv-python: For real-time video capture and frame manipulation.
* boto3: The official AWS SDK for Python, used to communicate with Rekognition and S3.
* awscli: The command-line interface for managing your AWS account services.

## ⚙️ Step 1: AWS Configuration

You must link your local machine to your AWS account. Open your terminal and run:
```bash
 aws configure
 ```
When prompted, enter your Access Key ID, Secret Access Key, your preferred Region (e.g., us-east-1) and set your Default output format to json.

## 🚀 Step 2: Collection & Identity Indexing

AWS Rekognition uses "Collections" to store facial feature vectors.

### Create the Collection:

```bash 
aws rekognition create-collection --collection-id "authorized-users"
```
### Index Your Identity:

Save a clear photo of yourself as **me.jpg** and run the registration script to add your face to the database.

## 🚀 Step 3: Running the Simulation

Execute the main recognition script:
```bash
python webcam_test.py
```
### Controls:

* Space: Capture a frame and send it to AWS for verification.
* ESC: Exit the simulation.


