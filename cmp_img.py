import face_recognition
import cv2
import sys

class CompareImg:

    def __init__(self,k_img,u_img):
        self.k_img = k_img
        self.u_img = u_img
    
    def cmp_img(self):
        know_img = cv2.imread(self.k_img)
        rgb_know_img = cv2.cvtColor(know_img,cv2.COLOR_BGR2RGB)
        # Error handling 
        try:
            know_img_encording = face_recognition.face_encodings(rgb_know_img)[0]
        except IndexError as e:
            print("Sample image face recognition failed")
            sys.exit(1)
            
        unknown_img = cv2.imread(self.u_img)
        rgb_unknown_img = cv2.cvtColor(unknown_img,cv2.COLOR_BGR2RGB)
        
        # Error handling
        try:
            unknown_img_encordings = face_recognition.face_encodings(rgb_unknown_img)
        except IndexError as e:
            print("Face recognition failed")
            return False
        
        # multiple faces check
        for unknown_img_encording in unknown_img_encordings:
            matches = face_recognition.compare_faces([know_img_encording],unknown_img_encording)[0]

            if matches:
                return True
        
        return False