#!/usr/bin/python3

from fastai.vision import *
import sys

image = sys.argv[1]


defaults.device = torch.device('cpu')

img = open_image(image)
learn = load_learner('.')

pred_class,pred_idx,outputs = learn.predict(img)
print(pred_class)

