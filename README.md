# Simple gamer 🎮🕹
 A simple code that can play a Telegram mini game using image processing.
 
 Watch [the video](https://youtu.be/ENYo6G_4h3w) on YouTube

# Image processing steps
First of all, we have to grab the screen image in order to be able to work with it:

```python
original_image = np.array(ImageGrab.grab(bbox=(380,140,445,520)))
```

The ```bbox``` parameter sets the coordination that you want to grab. The origin is the top-left corner of your screen.

Then by passing the ```original_image``` variable to ```process_img(...)```, we start processing.

The result of this step:

![raw](git_images/110_0_raw.jpg?raw=true "Raw")

The prosecc contains 4 steps:
## 1- Grayscale
Converts the colorfull image to a grayscale image:
```python
processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
```
![grayscaled](git_images/110_1_grayScaled.jpg?raw=true "Grayscale")

## 2- Threshold
Applys a threshold to the image. If a pixel is more than 250 it will be replaced with 255. Otherwise will be replaced with 0.
```python
ret, processed_img = cv2.threshold(processed_img, 250, 255, cv2.THRESH_BINARY)
```
![first-threshold](git_images/110_2_firstThreshold.jpg?raw=true "First threshold")

## 3- Convolutional filter
We know if a signal will be convolved to itself, the output of this convlution has tha maximum possible value. So in this step I convolve the screen image to a simple white circle. After this I expect to see some white blured areas at the ball position.
```python
path = os.getcwd()
kernel_path   = os.path.join(path, 'cir.png')
kernel = np.array(cv2.imread(kernel_path))
kernel = cv2.cvtColor(kernel, cv2.COLOR_BGR2GRAY)
kernel = kernel/(kernel.sum())  

processed_img = cv2.filter2D(processed_img, -1, kernel)
```
![convolution](git_images/110_3_convolution.jpg?raw=true "Convolutional filter")

As you see, a halo exists at the ball position.

## 4- Another threshold
Still we aren't sure about the exact ball position because of the other stuffs in the screen like that big "GOAL" text and colored papers. So I applied another threshold to the image: 
```python
ret, processed_img = cv2.threshold(processed_img, 50, 255, cv2.THRESH_BINARY)
```
![final](git_images/110_4_secondThreshold.jpg?raw=true "Final")

# Deciding when to click 
This game is so simple and easy. If the ball reach to a certain area you to click on the screen. I used a summation of pixel colors. If the summation was greater than 10*255 it means the ball is in the right position. So click!

- - - -
## Contact
[Telegram](http://t.me/s_motlaq) or E-mail: motlaq@aut.ac.ir
