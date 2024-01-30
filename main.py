import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import argparse
def write_to_csv(data, output_file):
    with open(output_file, 'a') as file:
        file.write(data + '\n')

def detect_qr_codes(image_path):
    data = decode((image_path), symbols=[ZBarSymbol.QRCODE])
    return data

def extract_frames(video_path, output_file):
    vidObj = cv2.VideoCapture(video_path)
    count = 0
    frame_counter = 0
    success = 1
    while success:
        success, image = vidObj.read()
        if success:
            frame_counter += 1
            if frame_counter % 60 == 0:
                valuesDecoded = detect_qr_codes(image)
                if len(valuesDecoded) != 0:
                    write_to_csv(valuesDecoded[0].data.decode('utf-8'), output_file)
            count += 1
    vidObj.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='QR Code Reader')
    parser.add_argument('video_path', type=str, help='Path to the input video file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_file)
