#read all the images from the train directory 
#where the train directory has the follwing folder containing the subfolder of each emotion 
train_dir=r"F:\it18021\archive\train"
classes=['angry','disgust','fear','happy','neutral','sad','surprise']
for category in classes:
    path= os.path.join(train_dir,category)
    for img in os.listdir(path):
        img_arr=cv2.imread(os.path.join(path,img))
        plt.imshow(cv2.cvtColor(img_arr,cv2.COLOR_BGR2RGB))
        plt.show()
        
        break
    break
