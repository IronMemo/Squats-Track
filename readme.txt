Squats Counter
This program utilizes various libraries to develop a real-time squat counting application using computer vision. It detects the positions of the body using the Mediapipe library, processes the images using OpenCV, and performs mathematical calculations with the help of the Math library.

Libraries Used
cv2 (OpenCV): Open Source Computer Vision library used for image processing and webcam functionality.
math: Provides advanced mathematical functions.
mediapipe: Offers a set of tools and algorithms for facial analysis, motion detection, and body pose recognition.
sys: Provides access to various system-specific variables and functions.
Functionality
The program captures and processes real-time video frames from a selected source. It detects the body pose landmarks and calculates the angle between the hips and knees for each leg. The program then checks if the squat repetition is performed correctly based on the defined angle range. The correct repetitions are counted, and when the desired number of squats is reached, a congratulatory message is displayed.

The program allows users to reset the squat counter by pressing the 'r' key and exit the application by pressing the ESC key.

Prerequisites
To run this program, ensure that you have the following libraries installed:

OpenCV (cv2)
Mediapipe
NumPy
Usage
Run the program.
Enter the desired number of squats when prompted.
Stand in front of the camera and perform squats, making sure the body pose is clearly visible.
The application will display the live video feed with annotated landmarks and the current number of correct repetitions.
Once the desired number of squats is achieved, a congratulatory message will appear on the screen.
Feel free to customize and modify the code to suit your needs. Happy squatting!

Note: Make sure to set the correct index for the webcam in the cap = cv2.VideoCapture(1) line if you are using a different camera source.