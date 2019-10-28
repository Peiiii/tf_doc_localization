## 表格提取

- 快速测试

运行命令:
python test.py
处理演示图片并显示结果
python main.py data/demo/1.jpg result.jpg
处理单张图片
python main.py data/demo data/results
处理一个文件夹下的图片，保存结果到另一文件夹

- 使用示例
```python
from test import Detector
D=Detector()
img=D.predict_from_file('data/demo/1.jpg')
D.save(img,'result.jpg')
```

- 原理说明
> 使用基于深度学习的关键点检测方法检测文档图像的四个角点，再对其进行透视变换和裁剪，得到文档区域。
   
