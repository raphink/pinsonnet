#!/usr/bin/python3

from fastai.vision import *
import sys
import warnings

defaults.device = torch.device('cpu')
learn = load_learner('.')
warnings.simplefilter("ignore")

for image in sys.argv[1:]:
    img = open_image(image)
    pred_class,pred_idx,outputs = learn.predict(img)
    print('%s: %s (%.2f%%)' % (image, pred_class, outputs.max()*100))
