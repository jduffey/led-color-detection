from PIL import Image
import numpy as np
import scipy.cluster
import binascii


IMAGE_DIRECTORY = 'images'
NUM_CLUSTERS = 5


def get_dominant_RGB_value(image):
    im = Image.open(image)
    im = im.resize((150, 150))  # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    codes, _ = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, _ = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, _ = np.histogram(vecs, len(codes))       # count occurrences

    index_max = np.argmax(counts)                    # find most frequent
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
