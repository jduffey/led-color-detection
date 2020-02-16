from utils import *

img_dir = 'images/'

red_imgs = [img_dir + 'red_square.png',
            img_dir + 'red_square_blur.png',
            img_dir + 'red_square_plus.png']

green_imgs = [img_dir + 'green_square.png',
              img_dir + 'green_square_blur.png',
              img_dir + 'green_square_plus.png']

blue_imgs = [img_dir + 'blue_square.png',
             img_dir + 'blue_square_blur.png',
             img_dir + 'blue_square_plus.png']

white_imgs = [img_dir + 'white_square.png',
              img_dir + 'white_square_blur.png',
              img_dir + 'white_square_plus.png']


def test_detect_red_images():
    for image in red_imgs:
        assert True == is_red(image)
        assert False == is_green(image)
        assert False == is_blue(image)
        assert False == is_white(image)


def test_detect_green_images():
    for image in green_imgs:
        assert False == is_red(image)
        assert True == is_green(image)
        assert False == is_blue(image)
        assert False == is_white(image)


def test_detect_blue_images():
    for image in blue_imgs:
        assert False == is_red(image)
        assert False == is_green(image)
        assert True == is_blue(image)
        assert False == is_white(image)


def test_detect_white_images():
    for image in white_imgs:
        assert False == is_red(image)
        assert False == is_green(image)
        assert False == is_blue(image)
        assert True == is_white(image)
