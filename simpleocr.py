import cv2
import pytesseract
from PIL import Image

# 定义图像文件路径
img_path = 'target_image.jpg'

# 读取图像文件
img = cv2.imread(img_path)

# 图像灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 图像二值化
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# 使用Tesseract OCR引擎识别图像中的文字
text = pytesseract.image_to_string(Image.fromarray(binary), lang='eng')

# 打印识别结果
print(f'Text: {text}')

# 使用OpenCV库实现图像识别
# 定义目标图像文件路径
target_img_path = 'test_image.jpg'

# 读取目标图像文件
target_img = cv2.imread(target_img_path)

# 使用SIFT算法检测关键点和特征描述符
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(target_img, None)

# 使用FLANN算法进行特征匹配
flann = cv2.FlannBasedMatcher()
matches = flann.knnMatch(des1, des2, k=2)

# 筛选出优秀的匹配点
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# 绘制匹配结果
result_img = cv2.drawMatches(img, kp1, target_img, kp2, good_matches, None, flags=2)

# 显示识别结果
cv2.imshow('Result Image', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()