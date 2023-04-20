from PIL import Image, ImageDraw  # Pillow Image Library
import cv2  # Opencv For Computer Vision
import numpy as np
from DbConnection import DbRetrieve, DbConnection


def show_prediction_labels_on_image(frame, predictions):
    conn = DbRetrieve()
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    regNo = None

    for name, (top, right, bottom, left) in predictions:
        # enlarge the predictions for the full sized image.
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 80, 255), width=2)

        # There's a bug in Pillow where it blows up with non-UTF-8 text
        # when using the default bitmap font

        regNo = str(name).lower().split("_")
        regNo = "/".join(regNo)
        name = name.encode("UTF-8")
        faceName = regNo
        try:
            faceName = conn.fillRecognitionData(str(regNo).upper())[0][0]
            markAttendance(regNo)

        except:
            pass

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 30, 255), outline=(0, 30, 255))
        draw.text((left + 6, bottom - text_height - 5), faceName, fill=(255, 255, 255, 255))

    # Remove the drawing library from memory as per the Pillow docs.
    del draw
    # Save image in open-cv format to be able to show it.

    opencvimage = np.array(pil_image)
    return opencvimage, regNo


def markAttendance(regNo):
    conn = DbConnection()
    if conn.addAttendance(regNo):
        print("Added to attendance successfully")
    else:
        print("Already signed")
