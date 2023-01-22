import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def overlay_image():
    # Create a window and trackbar for the slider
    cv2.namedWindow("Overlay")
    cv2.createTrackbar("Alpha", "Overlay", 0, 100, lambda x: None)

    # Open a file dialog to select the first image
    Tk().withdraw()
    img1_path = askopenfilename()
    img1 = cv2.imread(img1_path)
   
    # Open a file dialog to select the second image
    img2_path = askopenfilename()
    img2 = cv2.imread(img2_path)

    while True:
        # Get the current slider value
        slider_val = cv2.getTrackbarPos("Alpha", "Overlay") / 100

        # Overlay the two images using the slider value
        img = cv2.addWeighted(img1, slider_val, img2, 1 - slider_val, 0)

        # Display the overlayed image
        cv2.imshow("Overlay", img)

        # Exit the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

overlay_image()