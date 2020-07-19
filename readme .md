# Number-Plate-Recognition


Number  plate Recognition built using python, anaconda, opencv and tesseract



This system will store the license plate along with the date and store it in a csv file.
# Versions
Anaconda 4.3.0
Python 3.6
Opencv 3.4
Tesseract 4
Pandas 0.2
Streamlit 0.55.0



##Steps:

## Getting Started

Using a python3 (preferably 3.7) environment, run the following to install all the libraries used in this repository:

pip install -r requirements.txt

Recommend using conda as a CMD.



### Manual Install
 
Recommend using [Anaconda](https://www.anaconda.com/distribution/). Anaconda does not come with TensorFlow or Keras so you will need to install those seperately. 

pip install pandas numpy streamlit tensorflow keras

For additional information on installing TF & Keras: [TensorFlow](https://www.tensorflow.org/install), [Keras](https://keras.io/#installation)

For additional information on Streamlit: [Docs](https://streamlit.io/docs/)



### Training Models

You can either train your own model inside the Streamlit app or from the command line using training.py. The model.h5 and weights.h5 files are too large to include in this repository.

You must go to training.py change the path to train_data_path and validation_data_path to your path to training and validation images. 

You must also go to Main.py and change "Path to your images" to the path to your validation images where you have your test images saved.


### Running Streamlit App

From command line navigate to your application's directory and use:

streamlit run main.py



