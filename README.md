# modal-maker


### How to train modal 

Modal training is very GPU heavy so it's recomend using 
[Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true)

[Whats google colab? ](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d)
TL;DR its free GPU from Google




#### Training 

1. Prepare your dataset and zip it. Sample dataset can be found on this repo 
f you want to prepate your own dataset [read this](https://medium.com/deepquestai/object-detection-training-preparing-your-custom-dataset-6248679f0d1d). Its not hard but time consuming 

2. Go to Google Colab and create new Python 3 notebook 

3. Downloand your dataset with commad 

```buildoutcfg
!wget http://url.com/mydataset.zip
```

Unzip the modal 

```buildoutcfg
!unzip mydataset.zip
```

4. Install _tensorflow-gpu==1.13.1_

Tensefrow that comes out of the box with notebook has some problem with itself, and therefore has to be udpated. Sure google will fix that in the future but for now run
```buildoutcfg
!pip3 install tensorflow-gpu==1.13.1
```
  If you get a prompt to restart notebook, do it. 

5. Install [Image AI](https://github.com/OlafenwaMoses/ImageAI)
 
 Library that supports ML object detection, video detection, object tracking AND 4 different algoritms for model training wohoo! Also it supports YOLOv3
```buildoutcfg
!pip3 install imageai --upgrade
```

6. To make sure the custom model has better accuracy we can transfer  learning form a pre-trained YOLOv3 model. Transfer learning is very 
useful for small datasets.
*I dont fully understand how that works, but will found out*

```buildoutcfg
!wget https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5
```

7. Run the code from *scripts/training_code.py*

