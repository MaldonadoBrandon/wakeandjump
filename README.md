# Wake and jump!

###### Computer-Vision project fueled with Machine Learning framework of an innovative alarm clock that forces you to do *Jumping-Jacks* to stop the alarm

![](https://user-images.githubusercontent.com/98501536/280554059-2585fb59-6cc2-48ef-91b2-76b73ff7fd8e.png)

##Dependancies

- Python 3.10.2
- OpenCV
- Mediapipe
- Numpy
- Tkinter

##Overview

Wake and Jump is a Python project that works with OpenCV and [Mediapipe Framework](https://developers.google.com/mediapipe/solutions "Mediapipe Framework") to detect the bodyparts positions and calculate the number of Jumping Jacks performed by the user.
Once the user completed the goal number of jumps, the alarm will stop.

The following steps were performed for jump detection:

1. Capture the camera image and convert it into a NumPy array.
2. Apply the Mediapipe Pose Detection model to estimate the (x, y) positions of key body parts such as elbows, shoulders, hips, and knees.
3. Compute the distances between these body parts to assess their relative positions.
4. Utilize trigonometry to determine the angles formed between the different body parts.
5. Based on the positions of body parts and the calculated angles, evaluate if the user has executed a "Jumping Jack" exercise, and increment the counter accordingly.
