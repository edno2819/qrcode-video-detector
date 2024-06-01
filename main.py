import cv2
from pyzbar.pyzbar import decode, ZBarSymbol


def write_to_csv(data, output_file):
    try:
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
    except Exception as e:
        print(f"Failed to write to CSV: {e}")


def detect_qr_codes(image):
    try:
        data = decode(image, symbols=[ZBarSymbol.QRCODE])
        return data
    except Exception as e:
        print(f"Failed to decode QR codes: {e}")
        return []


def extract_frames(video_path, output_file):
    try:
        vidObj = cv2.VideoCapture(video_path)
        frame_counter = 0
        success = True
        while success:
            success, image = vidObj.read()
            if success:
                frame_counter += 1
                if frame_counter % 60 == 0:
                    valuesDecoded = detect_qr_codes(image)
                    if len(valuesDecoded) != 0:
                        write_to_csv(valuesDecoded[0].data.decode(
                            'utf-8'), output_file)
            else:
                print("Erro finding or reading the video!")

        vidObj.release()
    except Exception as e:
        print(f"Error processing video: {e}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='QR Code Reader')
    parser.add_argument('video_path', type=str, help='Path to the input video file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_file)
