FROM tensorflow/serving:2.7.0 

COPY clothing_model /models/clothing_model/1 
ENV MODEL_NAME="clothing_model"