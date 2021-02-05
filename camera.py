import cv2
import random
import numpy as np
import pandas as pd
from datetime import date
from mimics import Decision
from third_page import ThirdPage



detect = Decision()
page = ThirdPage()
cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

df = pd.read_excel('passwords.xls')
Id = df['Id']
Password0 = df['Password0']
Password1 = df['Password1']
Password2 = df['Password2']
Password3 = df['Password3']
length = len(df)

i = random.randint(0,100)
counter = 1
store = [0, 0, 0]
array_control = np.array([1, 1, 1])
control_array = np.array([0, 0, 0, 0])

while True:
    k = cv2.waitKey(500)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        password = [Password0[counter], Password1[counter], Password2[counter], Password3[counter]]
        index = password.index(1)
        array = np.array(password)
        detect.refresh(frame, index)
        detect.password(array)
        check_array = detect.control()
        if (check_array == control_array).all():
            print("bekleme")
        else:
            get = detect.compare()
            store[counter - 1] = get
            print(store)
            counter += 1
            if counter == length:
                array_result = np.array(store)
                if (array_result == array_control).all():
                    key = 1
                    counter = 1
                    store = [0, 0, 0]
                    print("Login Confirmed")
                    page.refresh(key)
                    cv2.imwrite("faces/User." + str(i) + "-" + str(date.today()) + ".jpg", gray[y:y + h, x:x + w])
                    i += 1
                    k = 1


                else:
                    key = 0
                    print("Entry Denied")
                    page.refresh(key)
                    counter = 1
                    store = [0, 0, 0]
                    k = 1

    cv2.imshow('frame', frame)
    if k == 1:
        break



cap.release()
cv2.destroyAllWindows()
