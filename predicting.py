import cv2, numpy as np
from keras.models import load_model

model = load_model("face-mask-detection-model.h5")

def is_masked(path = None,photo = None):
    labels = {0 : "without mask", 1 : "with mask"}
    size = 4
    classifier = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
    if photo == None:
        photo = cv2.imread(path)
    img =cv2.flip(photo,1,1) #Flip to act as a mirror
    # Resize the image to speed up detection
    mini = cv2.resize(img, (img.shape[1] // size, img.shape[0] // size))
    # detect MultiScale / faces 
    faces = classifier.detectMultiScale(mini)
    # show the final result 
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        #Save just the rectangle faces in SubRecFaces
        face_img = img[y:y+h, x:x+w]
        resized=cv2.resize(face_img,(96, 96))
        normalized=resized/255.0
        reshaped=np.reshape(normalized,(1,96, 96,3))
        reshaped = np.vstack([reshaped])
        result=model.predict(reshaped)
        
        label=np.argmax(result,axis=1)[0] # extract the result
        return labels[label]