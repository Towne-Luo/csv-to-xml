#SSD网络数据集格式转换
## 说明
SSD网络在训练是，对数据集的文件格式要求为：

               ---datasetfolder
                    ---Annotations
                    ---ImageSets
                    ---JPEGImages
三个文件夹分别用来存放`标注-Annotations`、`训练/测试集划分-ImageSets`、`图片-JPEGImages`

但有的时候数据集的标注信息是以`.csv`的形式给出，此时就需要对格式进行简单转换。以[PN9](PN9)数据集为例。
## 步骤
1.读取`.csv`文件，按照病人CT图像名生成`.xml`文件的文件名
2.根据SSD模型需要的信息，创建对应的节点，并生成`.xml`文件
3.根据`.xml`文件名寻找对于的CT图像，并放到统一的路径`JPEGImages`下
## 使用方法
1.git clone 

2.将代码中的文件路径改为自己的文件
