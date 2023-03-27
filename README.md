# simpleocr
简单的文字和图片识别项目
# 使用说明
该项目使用了OpenCV、Pytesseract和Pillow三个Python库，请确保您已经正确安装了这些库。
# 项目功能
使用OpenCV库读取图像文件，将图像转换为灰度图像，并对灰度图像进行二值化处理。

使用Tesseract OCR引擎对二值化后的图像进行文字识别。

使用OpenCV库实现图像的特征匹配，包括使用SIFT算法检测关键点和特征描述符，并使用FLANN算法进行特征匹配，筛选出优秀的匹配点。

使用OpenCV库绘制匹配结果，并将结果显示出来    
