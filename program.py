import face_recognition as fr
from PIL import Image,ImageDraw

img1=fr.load_image_file("class.png")
img2=fr.load_image_file("student1.png")
img3=fr.load_image_file("student2.png")
img4=fr.load_image_file("student3.png")
img5=fr.load_image_file("student4.png")

location=fr.face_locations(img1)
class_encodings_1=fr.face_encodings(img1)

faces_detected = len(location)
if faces_detected == 0:
    print("No students detected")
print("Faces detected:", faces_detected)

pil_image = Image.fromarray(img1)
draw=ImageDraw.Draw(pil_image)

count = 0 

#student1
student_encoding=fr.face_encodings(img2)

if len(student_encoding) > 0:
    matches = fr.compare_faces(class_encodings_1, student_encoding[0])
    
    if True in matches:
        print("Student 1 - Present")
        count += 1

        for i, match in enumerate(matches):
            if match:
                top, right, bottom, left = location[i]
                draw.rectangle(((left, top), (right, bottom)),outline="green", width=3)
    else:
        print("Student1 - Absent")

#student2
student_encoding = fr.face_encodings(img3)

if len(student_encoding) > 0:
    matches = fr.compare_faces(class_encodings_1, student_encoding[0])

    if True in matches:
        print("Student2 - Present")
        count += 1

        for i, match in enumerate(matches):
            if match:
                top, right, bottom, left = location[i]
                draw.rectangle(((left, top), (right, bottom)),outline="green", width=3)
    else:
        print("Student2 - Absent")

#student3
student_encoding = fr.face_encodings(img4)

if len(student_encoding) > 0:
    matches = fr.compare_faces(class_encodings_1, student_encoding[0])

    if True in matches:
        print("Student3 - Present")
        count += 1

        for i, match in enumerate(matches):
            if match:
                top, right, bottom, left = location[i]
                draw.rectangle(((left, top), (right, bottom)),outline="green", width=3)
    else:
        print("Student3 - Absent")
        
#student4
student_encoding = fr.face_encodings(img5)

if len(student_encoding) > 0:
    matches = fr.compare_faces(class_encodings_1, student_encoding[0])

    if True in matches:
        print("Student3 - Present")
        count += 1

        for i, match in enumerate(matches):
            if match:
                top, right, bottom, left = location[i]
                draw.rectangle(((left, top), (right, bottom)),outline="green", width=3)
    else:
        print("Student3 - Absent")

print("Students Present:", count, "out of 4")

pil_image.save("attendance.png")
pil_image.show()