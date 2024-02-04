# A python script to detect and read QR codes from a video!

[![python](https://img.shields.io/badge/Python-3.12.1-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![opencv](https://img.shields.io/badge/OpenCV-4.9.0.80-5C3EE8.svg?style=flat&logo=opencv&logoColor=white)](https://opencv.org)
[![pyzbar](https://img.shields.io/badge/pyzbar-0.1.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://pypi.org/project/pyzbar)
[![numpy](https://img.shields.io/badge/Numpy-1.26.3-013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org)
[![pandas](https://img.shields.io/badge/Pandas-2.2.0-150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-4285F4.svg?style=flat&logo=git&logoColor=white)](https://opensource.org/licenses/MIT)

---

## Description

This script uses OpenCV and pyzbar to detect and read QR codes from a video. The script will read a image for every 60 frames, find the QR codes found and decode to write in the output file, one code for each line.

You can adjust the reading frequency by changing the `frame_counter % 60` in line 21 in the `main.py` file.

## Requirements

- Pipenv
- Python 3

## Dependencies installation

```bash
pipenv install
```

## Usage

```bash
pipenv run python main.py <video_path> <output_textfile>
```
