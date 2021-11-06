# import shutil
# old_path = 'train_img_01/00001/00001_0148.jpg'
# new_path = 'PN9_NEW/JPEGImages/'
# shutil.copy(old_path,new_path)
#
name = '1'
for i in range(148, 150):
    new_name = (5 - len(name)) * '0' + name + '_' + str(i)
    print(new_name)

