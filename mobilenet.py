import onnxruntime as ort
import numpy as np
from helper import *


CLASS_NAME = ['cat','dog']

def regconition(MODEL_TF2ONNX_DIR, img_path):
    #Read image (160,160,3)
    img = readImg(img_path).astype(np.float32)

    #Batch (1,160,160,3)
    img_batch = np.expand_dims(img, axis=0)
    #print(img_batch.shape)
    # #Load ONNX model and run sample inference
    sess = ort.InferenceSession(MODEL_TF2ONNX_DIR)
    
    input_name = sess.get_inputs()[0].name
    output_name = sess.get_outputs()[0].name

    result = sess.run([output_name],{input_name: img_batch})
    sigmoid = lambda x: 1./(1+ np.exp(-x))

    preds = sigmoid(result[0])
    preds = np.where(preds < 0.5, 0,1)
    preds = np.squeeze(preds)
    label = CLASS_NAME[preds]
    print(label)

    show_img(img,label)


if __name__ == "__main__":
    regconition('./model.onnx', './sample2.jpg')



