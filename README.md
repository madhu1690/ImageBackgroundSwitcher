# Green Screen Replacement Script

This script replaces a green screen background in an image with a new background image using OpenCV.

## Prerequisites

- Python 3.x
- OpenCV
- Numpy

## Installation

1. **Install Python**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install OpenCV and Numpy**: Install the required Python packages using pip:
    ```sh
    pip install opencv-python numpy
    ```

## Usage

1. **Prepare your images**:
    - `pic 1.png`: This is the image with the green screen background.
    - `pic 2.jpg`: This is the new background image.

2. **Place the images**: Ensure the images are placed in the specified path on your system. Update the paths in the script if necessary.

3. **Run the script**: Execute the script using Python:
    ```sh
    python replace_green_screen.py
    ```

## Script Explanation

The script performs the following steps:

1. **Load the images**: The script reads the images from the specified paths.
    ```python
    img = cv2.imread(r"C:\Users\s\OneDrive\Desktop\manjunath\pic 1.png")
    bg = cv2.imread(r"C:\Users\s\OneDrive\Desktop\manjunath\pic 2.jpg")
    ```

2. **Resize the background**: The background image is resized to match the size of the original image.
    ```python
    bg = cv2.resize(bg, (img.shape[1], img.shape[0]))
    ```

3. **Convert to HSV**: The original image is converted to the HSV color space.
    ```python
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ```

4. **Create a mask**: A mask is created to isolate the green screen background.
    ```python
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    ```

5. **Invert the mask**: The mask is inverted to isolate the foreground.
    ```python
    mask_inv = cv2.bitwise_not(mask)
    ```

6. **Mask the original image**: The foreground is extracted using the inverted mask.
    ```python
    fg = cv2.bitwise_and(img, img, mask=mask_inv)
    ```

7. **Mask the background**: The background is masked to fit into the green screen area.
    ```python
    bg_masked = cv2.bitwise_and(bg, bg, mask=mask)
    ```

8. **Combine images**: The foreground and the masked background are combined to create the final image.
    ```python
    result = cv2.add(fg, bg_masked)
    ```

9. **Display the results**: The original, masked, and final images are displayed.
    ```python
    cv2.imshow('Original Image', img)
    cv2.imshow('Masked Image', fg)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

## Troubleshooting

- **Incorrect paths**: Ensure the paths to the images are correct.
- **Library issues**: Make sure OpenCV and Numpy are installed correctly.
- **Green screen color range**: Adjust the `lower_green` and `upper_green` values if your green screen color is not properly detected.

## License

This project is licensed under the MIT License.
