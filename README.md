# Face Align-and-crop With Adjustable Margin

> This demo is originally from https://github.com/nlhkh/face-alignment-dlib.

#### Setup:

1. Run `pip install -r requirements.txt`
2. Download and extract shape predictor 68 landmarks at this [link](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).
3. Place the extracted predictor in the root directory of this project.
4. Find some images with faces.

#### Run:

```
python facecrop.py \<image input\> \<image output\> -m 1.5 -s 1
```

`m` represent margin around the face, default is 1.5, s represent scale, default is 1.

#### Results

**image input**

![Messi](D:\Algorithms\face-align-and-crop-with-adjustable-margin\Messi.jpg)

**image output**

![res](D:\Algorithms\face-align-and-crop-with-adjustable-margin\res.jpg)


##### Dependencies:

- [dlib](http://dlib.net/)
- [opencv-python](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)