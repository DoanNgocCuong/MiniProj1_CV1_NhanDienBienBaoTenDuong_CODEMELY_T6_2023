# anh Tú
'''
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
import sys
import argparse
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter lang as ch, en, french, german, korean, japan
# to switch the language model in order.

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = 'PaddleOCR')
    
    parser.add_argument(
        "--source", 
        default="0", 
        type=str
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    ocr = PaddleOCR(use_angle_cls=True, lang='vi') # need to run only once to download and load model into memory
    img_path = args.source
    results = ocr.ocr(img_path, cls=True)
    text_recog = []
    confidence = 0
    count = 0
    for result in results:
        # print(result)
        text_recog.append(result[1][0])
        confidence += result[1][1]
        count+=1

    text = ' '.join(text_recog)
    confidence = confidence /count

    print(text, round(confidence,2))

if __name__ == '__main__':
    main()
    sys.exit(0)

# cách chạy là : python main.py --source <pathtoimage>
# pathtoimage la cai duong dan vao cai file hinh text
# python main.py --source cropped_image_0.9489.jpg
'''

from paddleocr import PaddleOCR
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='PaddleOCR')
    parser.add_argument("--source", default="0", type=str)
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    ocr = PaddleOCR(use_angle_cls=True, lang='vi')  # need to run only once to download and load model into memory
    img_path = args.source
    results = ocr.ocr(img_path, cls=True)

    text_recog = []
    total_confidence = 0
    count = 0

    for line in results:
        for result in line:
            # result is a tuple (box, (text, confidence))
            text = result[1][0]
            confidence = result[1][1]
            text_recog.append(text)
            total_confidence += confidence  # Accumulate the confidences
            count += 1

    text = ' '.join(text_recog)
    average_confidence = total_confidence / count if count else 0  # Calculate the average

    print(text, round(average_confidence, 2))

if __name__ == '__main__':
    main()
# python newmain_aTu.py --source cropped_image_0.9489.jpg