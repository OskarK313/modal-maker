from imageai.Detection.Custom import DetectionModelTrainer


# Create instance of Detection Model Trainer and set the model to YOLOv3
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()

# Directory url to dataset
trainer.setDataDirectory(data_directory="hololens")

# Config file for dataset
# Object_name_array = name for our dataset
# batch_size = The larger the better, but Google colab limitits the max to 4. Sample values 2, 4, 8, 16, 24, 48 etc
# num_experiments = Number of iterations on custom dataset
# train_from_pretrained_model = This is used to leverage transfer learning using the pretrained YOLOv3 model
trainer.setTrainConfig(object_names_array=["hololens"], batch_size=4, num_experiments=100, train_from_pretrained_model="pretrained-yolov3.h5")

# Start learning
trainer.trainModel()
