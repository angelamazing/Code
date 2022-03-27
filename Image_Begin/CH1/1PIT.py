import os
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

filelist = os.listdir(os.getcwd() + '\image')


def toJpg():
    for infile in filelist:
        outfile = os.path.splitext(infile)[0] + ".jpg"
        print(os.path.splitext(infile)[1])
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print("cannot convert", infile)


im = array(Image.open(os.getcwd() + '\image' + '\p (1).jpg').convert('L'))  # 读取图像到数组

gray()

subplot(121)
axis('off')  # 坐标轴不显示
imshow(im)

# sigma = 3
#
# imx = zeros(im.shape)
# imx = im + 0.4 * (im - filters.gaussian_filter(im, sigma))
# imx = clip(imx, 0, 255)
#
# subplot(122)
# axis('off')
# imshow(imx)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r*')
plot(x[:2], y[:2])

show()
