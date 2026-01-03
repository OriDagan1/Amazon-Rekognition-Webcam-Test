import cv2
import boto3

# Initialize Rekognition client
rekognition = boto3.client('rekognition')
cap = cv2.VideoCapture(0) # 0 is usually the built-in webcam

print("Press SPACE to verify identity, or ESC to quit.")

while True:
    ret, frame = cap.read()
    cv2.imshow('Security Camera Prototype', frame)

    key = cv2.waitKey(1)
    if key % 256 == 27: # ESC pressed
        break
    elif key % 256 == 32: # SPACE pressed
        # Convert frame to JPG bytes
        _, buffer = cv2.imencode('.jpg', frame)
        image_bytes = buffer.tobytes()

        # Search the collection for a match
        try:
            response = rekognition.search_faces_by_image(
                CollectionId='authorized-users',
                Image={'Bytes': image_bytes},
                MaxFaces=1,
                FaceMatchThreshold=90 # 90% confidence required
            )

            if response['FaceMatches']:
                name = response['FaceMatches'][0]['Face']['ExternalImageId']
                confidence = response['FaceMatches'][0]['Similarity']
                print(f"ACCESS GRANTED: Hello {name} ({confidence:.2f}% match)")
            else:
                print("ACCESS DENIED: Unknown person detected.")
        
        except Exception as e:
            print(f"Error: {e}")

cap.release()
cv2.destroyAllWindows()