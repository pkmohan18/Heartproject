# Heartproject

In this work, we take stethoscope sounds (and also heartbeat sounds recorded using the microphone of a mobile phone) as input and apply deep learning to the task of automated cardiac auscultation, i.e. recognizing abnormalities in heart sounds. We describe a novel algorithm which first transforms the one-dimensional time-series inputs into a two-dimensional time-frequency Melspectrograms. It then trains a 4-layer CNN model on the MFCC (Mel-Frequency Cepstral Coefficients) obtained from the Melspectrograms. The trained network automatically distinguish between normal and abnormal heartbeat sound inputs. We did not use any other time sequence based Neural Networks such as RNNs since the temporal behavior of the heartbeat was repeated within the window of observation and different sequential patterns were not needed to be learnt.

Our goal is to provide a reliable, fast and low-cost system that can be used by untrained frontline health workers or anyone with internet access, to help determine whether an individual should be referred for expert diagnosis, particularly in areas where access to clinicians and medical care is limited. This will also help in early diagnosis of CVDs which will drastically decrease the potential risk factors of these deaths.

The heartbeat audio file must be in .wav format

Download the dataset from [here](http://www.peterjbentley.com/heartchallenge/index.html).

Steps to run the project:

Step 1: Install VS Code and Install the required tools to run the project such as Django.
Step 2: Install XAMPP server to access phpMyAdmin SQL database.
Step 3: Open the project folder through VS Code.
Step 4: Open phpMyAdmin and create a MySQL database named patient_db.
Step 5: Open the terminal and run $ python manage.py migrate to migrate the database. 
Step 6: Run $ python manage.py migrate --run-syncdb to sync the database and create a table.
Step 7: Run the project using $ python manage.py runserver.
Step 8:  Open the web browser and go to http://127.0.0.1:8000/.
Step 9:  Register as a new user by providing login credentials.
Step 10:  Login to the system by using email and password.
Step 11: Upload the audio file of the heart beat in .wav format for detecting the Heartbeat anomaly.
Step 12: Get the prediction result as either Normal or Abnormal Heartbeat.     

