from imageai.Prediction import ImagePredication
import os

execution_path = os.getcwd()
predicaiton = ImagePredication()
predicaiton.setModelTypeAsSqueezeNet()
predicaiton.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
predicaiton.loadModel()

predicaitons, probabilities = predicaiton.predictImage(os.path.join(execution_path, 'giraffe.jpg'), result_count=5)
for eachPrediction, eachProbability in zip(predicaitons, probabilities):
    print(eachPrediction, " : ", eachProbability)