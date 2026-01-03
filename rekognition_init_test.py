import boto3

client = boto3.client('rekognition')

# Upload your photo to index it
with open("C:\\Users\\oripa\\Pictures\\Screenshot 2025-05-07 100006.png", 'rb') as image:
    response = client.index_faces(
        CollectionId='authorized-users',
        Image={'Bytes': image.read()},
        ExternalImageId='Ori', # Give yourself a label
        MaxFaces=1,
        QualityFilter="AUTO",
        DetectionAttributes=['ALL']
    )

print(f"Face indexed successfully. FaceID: {response['FaceRecords'][0]['Face']['FaceId']}")