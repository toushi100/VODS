# VODS
This project was built using :
- Django Framework
- Tensorflow
- SQLite

This is a website were the user can :
- Sign up / Sign in
- Upload Videos
- Delete their Videos
- Watch Videos
- Comment on any Video
- Change / update their information in the profile
- Search for Objects that appeared in the video


Installation :
 - git clone https://github.com/toushi100/VODS/
 - pip install -r requirements.txt
 - change the path to your virtual environment in VODS/SSD/tagroba.py


More info:
after the user uploads a video a one time processing starts
the video is passed to an object detection script.
I used <a href = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1">openimages_v4/ssd/mobilenet_v2</a> model
for more objects to be detected.
the output of the detection script is saved in a .pickle file 
then it is opened, converted into json and inserted in the DB
