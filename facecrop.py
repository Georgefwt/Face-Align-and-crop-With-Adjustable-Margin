import cv2, dlib, argparse
from utils import extract_left_eye_center, extract_right_eye_center, get_rotation_matrix, crop_image
from PIL import Image
import os
import glob

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Align faces in image')
    parser.add_argument('input', type=str, help='')
    parser.add_argument('output', type=str, help='')
    parser.add_argument('--scale', '-s', type=int, default=1, help='an integer for the accumulator')
    parser.add_argument('--margin', '-m', type=float, default=1.5, help='margin around the face')
    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output
    scale = args.scale
    margin = args.margin
    if not os.path.exists(output_folder):
        print("Creating output folder")
        os.makedirs(output_folder)

    img_files = glob.glob(input_folder + "/*")
    for img_file in img_files:
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        img = cv2.imread(img_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width = img.shape[:2]
        s_height, s_width = height // scale, width // scale
        img = cv2.resize(img, (s_width, s_height))

        dets = detector(img, 1)

        for i, det in enumerate(dets):
            shape = predictor(img, det)
            left_eye = extract_left_eye_center(shape)
            right_eye = extract_right_eye_center(shape)

            M = get_rotation_matrix(left_eye, right_eye)
            rotated = cv2.warpAffine(img, M, (s_width, s_height), flags=cv2.INTER_CUBIC)

            cropped = crop_image(rotated, det,margin)

            print(os.path.join(output_folder, os.path.basename(img_file)))
            cropped.save(os.path.join(output_folder, os.path.basename(img_file)))