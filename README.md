# Hand-Gesture-Controlled-Interactive-Presentation-System
Description:
This project is an innovative, gesture-based presentation controller that allows users to navigate slides and annotate presentations in real-time using hand gestures. Built with Python, OpenCV, and the CVZone hand tracking module, the system transforms any standard presentation into an interactive experience by detecting specific hand gestures to control slide navigation (moving forward/backward) and enabling freehand drawing on slides.

Key Features:
Gesture-Based Slide Navigation:
Move to the next slide by raising the pinky finger (gesture: [0,0,0,0,1]).
Go back to the previous slide by raising the thumb (gesture: [1,0,0,0,0]).

Real-Time Annotation Tool:
Draw freely on slides by pointing with the index finger (gesture: [0,1,0,0,0]).
Erase annotations by raising the index, middle, and ring fingers (gesture: [0,1,1,1,0]).
Smooth, natural drawing with no constrained areas—scribble anywhere on the slide.

Visual Pointer for Emphasis:
A red circular pointer appears when the user raises the index and middle fingers (gesture: [0,1,1,0,0]), helping highlight key points without drawing.

User-Friendly Interface:
Live webcam feed overlay on slides for real-time gesture feedback.
Green threshold line to indicate gesture activation zone.

Technologies Used:
Python (Primary language)
OpenCV (Real-time hand tracking and image processing)
CVZone (Hand detection and gesture recognition)
NumPy (Coordinate calculations)

Applications:
Interactive Presentations: Ideal for educators, business presenters, and public speakers.
Touchless Control: Useful in environments where hygiene or remote interaction is prioritized.
Accessibility: Helps users who prefer gesture-based input over traditional clickers.

Future Enhancements:
Integration with PowerPoint/Google Slides via APIs.
Multi-hand detection for collaborative annotations.
Voice command support for hybrid control.
