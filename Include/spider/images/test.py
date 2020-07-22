# from PIL import Image
#
#
# # 二值化处理
# def two_value():
#     # 打开文件夹中的图片
#     image = Image.open('1_2.jpg')
#     # 灰度图
#     lim = image.convert('L')
#     # 灰度阈值设为165，低于这个值的点全部填白色
#     threshold = 130
#     table = []
#
#     for j in range(256):
#         if j < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#
#     bim = lim.point(table, '1')
#     bim.save('1_3.jpg')
#
#
# two_value()



# from PIL import Image
#
# # 去除干扰线
# im = Image.open('1_1.jpg')
# # 图像二值化
# data = im.getdata()
# w, h = im.size
# black_point = 0
#
# for x in range(1, w - 1):
#     for y in range(1, h - 1):
#         mid_pixel = data[w * y + x]  # 中央像素点像素值
#         if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
#             top_pixel = data[w * (y - 1) + x]
#             left_pixel = data[w * y + (x - 1)]
#             down_pixel = data[w * (y + 1) + x]
#             right_pixel = data[w * y + (x + 1)]
#
#             # 判断上下左右的黑色像素点总个数
#             if top_pixel < 10:
#                 black_point += 1
#             if left_pixel < 10:
#                 black_point += 1
#             if down_pixel <  10:
#                 black_point += 1
#             if right_pixel < 10:
#                 black_point += 1
#             if black_point < 1:
#                 im.putpixel((x, y), 255)
#                 # print(black_point)
#             black_point = 0
#
# im.save('1_2.jpg')
#

import sys, os
from PIL import Image, ImageDraw


# 二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
# 该函数也可以改成RGB判断的,具体看需求如何
def getPixel(image, x, y, G, N):
    L = image.getpixel((x, y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None

    # 降噪


# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败
def clearNoise(image, G, N, Z):
    draw = ImageDraw.Draw(image)

    for i in range(0, Z):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                color = getPixel(image, x, y, G, N)
                if color != None:
                    draw.point((x, y), color)

                    # 打开图片


image = Image.open('1_2.jpg')

# 将图片转换成灰度图片
clearNoise(image, 50, 4, 4)
src = '1_5.jpg'
image.save(src)
