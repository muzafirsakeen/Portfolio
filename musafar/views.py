from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination
from django.http.response import StreamingHttpResponse
import cv2
from django.core.paginator import Paginator
from . models import Song,Datas
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.core.mail import send_mail

def homes(request):
    dests = Datas.objects.all()
    print(dests)
    return render(request,'index.html',{'dests':dests})



from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from keras.models import load_model
import cv2
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array

face_classifier = cv2.CascadeClassifier('static/files/haarcascade_frontalface_default.xml')
classifier = load_model('static/files/model.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

def emotion_detection(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():  # Check if video capture is successful
        return HttpResponse('Failed to open webcam')
    
    label = 'No Faces'  # Assign a default value
    
    while True:
        ret, frame = cap.read()
        if not ret:  # Check if video frame is read successfully
            break
        
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                break

        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if label == 'Neutral':
        return render(request,"project.html",context)
    elif label == 'Sad':
        return render(request,"project.html",context)
    elif label == 'Happy':
        return render(request,"project.html",context)
    elif label == 'Angry':
        return render(request,"project.html",context)
    elif label == 'Disgust':
        return render(request,"project.html",context)
    elif label == 'Fear':
        return render(request,"project.html",context)
    elif label == 'Surprise':
        return HttpResponse('Your Emotion is Surprise')

    return HttpResponse('No emotion detected')
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email
        send_mail(
            subject,
            f"Email: {email}\n\n{message}",
            email,
            ['musafarshakeel@gmail.com'],  # Add recipient email address(es)
            fail_silently=False,
        )

        # Redirect or display success message
        return render(request, 'proj.html')

    return render(request, 'index.html')