from keras import applications
import numpy as np


def main():
    model = applications.resnet50.ResNet50(include_top=False, weights='imagenet')
    
    x_train=np.load('')
    x_cv=np.load('')

    x_train_bottleneck = model.predict(x_train)
    x_test_bottleneck = model.predict(x_cv)

    np.save('x_train_resnet_bottleneck.npy', x_train_bottleneck)
    np.save('x_test_resnet_bottleneck.npy', x_test_bottleneck)


if __name__=='__main__':
    main()