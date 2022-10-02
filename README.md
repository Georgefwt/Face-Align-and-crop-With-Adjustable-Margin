# Face Align-and-crop With Adjustable Margin

> This demo is originally from https://github.com/nlhkh/face-alignment-dlib.

#### Setup:

1. Run `pip install -r requirements.txt`
2. Download and extract shape predictor 68 landmarks at this [link](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).
3. Download and extract shape predictor 5 landmarks at this [link](http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2).
4. Place the extracted predictor in the root directory of this project.
5. Find some images with faces.

#### Run:

```
python facecrop.py <image input folder> <image output folder> [-m 1.5] [-s 1]
```

`m` represent margin around the face, default is 1.5, `s` represent scale, default is 1.

#### Results

**image input**

![Messi](./Messi.jpg)

**image output**

![res](./res.jpg)


##### Dependencies:

- [dlib](http://dlib.net/)
- [opencv-python](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)