from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import binascii


IMAGE_DIRECTORY = 'images'
NUM_CLUSTERS = 5


def get_dominant_RGB_value(image):
    im = Image.open(image)
    im = im.resize((150, 150))  # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    hex_color = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')

    h = hex_color
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    
    return rgb


def is_red(image):
    rgb = get_dominant_RGB_value(image)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    return r > 160 and g < 100 and b < 140


def is_green(image):
    rgb = get_dominant_RGB_value(image)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    
    return r < 100 and g > 160 and b > 80


def is_blue(image):
    rgb = get_dominant_RGB_value(image)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    
    return r < 100 and g < 100 and b > 200


def is_white(image):
    rgb = get_dominant_RGB_value(image)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    
    return r > 180 and g > 180 and b > 180



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
        print(image)
        assert True == is_red(image)
        assert False == is_green(image)
        assert False == is_blue(image)
        assert False == is_white(image)


def test_detect_green_images():
    for image in green_imgs:
        print(image)
        assert False == is_red(image)
        assert True == is_green(image)
        assert False == is_blue(image)
        assert False == is_white(image)


def test_detect_blue_images():
    for image in blue_imgs:
        print(image)
        assert False == is_red(image)
        assert False == is_green(image)
        assert True == is_blue(image)
        assert False == is_white(image)


def test_detect_white_images():
    for image in white_imgs:
        print(image)
        assert False == is_red(image)
        assert False == is_green(image)
        assert False == is_blue(image)
        assert True == is_white(image)

test_detect_red_images()
test_detect_green_images()
test_detect_blue_images()
test_detect_white_images()