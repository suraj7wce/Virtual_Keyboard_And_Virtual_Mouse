import tkinter as tk
import subprocess
import os
from PIL import ImageTk, Image

def run_file1():
    print("Virtual Keyboard is running....")
    file_path = os.path.join(r'C:\Users\shree\Desktop\mp4\Virtual_Keyboard', 'virtual_keyboard.py')
    subprocess.run(['python', file_path])

def run_file2():
    print("Virtual Mouse is running....")
    file_path = os.path.join(r'C:\Users\shree\Desktop\mp4\Virtual_Mouse', 'virtual_mouse.py')
    subprocess.run(['python', file_path])

# Create the main window
window = tk.Tk()

# Load the image
image_path = r"C:\Users\shree\Desktop\mp4\static\img.jpeg"
image = Image.open(image_path)
image = image.resize((800, 500))  # Adjust the size as needed
image_tk = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=image_tk)
image_label.pack()

# # Create buttons for running the files
# button1 = tk.Button(window, text='Run File 1', command=run_file1)
# button1.pack()
#
# button2 = tk.Button(window, text='Run File 2', command=run_file2)
# button2.pack()
#
# # Start the GUI event loop
# window.mainloop()

button1 = tk.Button(window, text='Virtual Keyboard', command=run_file1, bg='lightblue', fg='black', font=('Arial', 16, 'bold'))
button1.place(x=500, y=150)  # Adjust the coordinates as needed

button2 = tk.Button(window, text='Virtual Mouse', command=run_file2, bg='lightgreen', fg='black', font=('Arial', 16, 'bold'))
button2.place(x=500, y=250)  # Adjust the coordinates as needed

# Start the GUI event loop
window.mainloop()



# import os
# from tkinter import *
# from Virtual_Keyboard.virtual_keyboard import *
# from Virtual_Keyboard.keys import *
# from Virtual_Keyboard.handTracker import *
# from Virtual_Mouse.virtual_mouse import *
# from Virtual_Mouse.HandTracking import *
#
# tkWindow=Tk()
# tkWindow.geometry('400x150')
# tkWindow.title('Suraj')
#
#
# # def v_mouse():
# #     os.system('python virtual_mouse.py')
# #
# #
# # def v_keyboard():
# #     os.system('python virtual_keyboard.py')
#
#
# button1=Button(tkWindow,text='Keyboard',command=funck())
# button1.grid(row=0,column=0)
#
# button2=Button(tkWindow,text='Mouse',command=funcm())
# button2.grid(row=1,column=1)
#
# tkWindow.mainloop()


# import tkinter as tk
# import subprocess
# from Virtual_Mouse import *
#
# def run_script():
#     # Replace "script.py" with the path to your Python script
#     subprocess.call(["python", "virtual_mouse.py"])
#
# # Create a new window
# window = tk.Tk()
# window.title("Run Script")
#
# # Create a button that runs the script when clicked
# button = tk.Button(window, text="Run Script", command=run_script)
# button.pack(pady=10)
#
# # Start the GUI event loop
# window.mainloop()

# import keras
# from keras.models import Sequential, Model
# from keras.layers import Dense, Dropout, Flatten, Conv3D, MaxPooling3D, Input
# from keras.optimizers import SGD
# from keras.callbacks import ModelCheckpoint
# import numpy as np
#
# # Define the Two-Stream CNN model
# def TwoStreamCNN(input_shape, num_classes):
#     # Spatial stream
#     spatial_model = Sequential()
#     spatial_model.add(Conv3D(64, kernel_size=(3, 3, 3), activation='relu', input_shape=input_shape))
#     spatial_model.add(MaxPooling3D(pool_size=(2, 2, 2)))
#     spatial_model.add(Conv3D(128, kernel_size=(3, 3, 3), activation='relu'))
#     spatial_model.add(MaxPooling3D(pool_size=(2, 2, 2)))
#     spatial_model.add(Conv3D(256, kernel_size=(3, 3, 3), activation='relu'))
#     spatial_model.add(Conv3D(256, kernel_size=(3, 3, 3), activation='relu'))
#     spatial_model.add(MaxPooling3D(pool_size=(2, 2, 2)))
#     spatial_model.add(Flatten())
#     spatial_model.add(Dense(512, activation='relu'))
#     spatial_model.add(Dropout(0.5))
#
#     # Temporal stream
#     temporal_input = Input(shape=input_shape)
#     temporal_model = Conv3D(64, kernel_size=(3, 3, 3), activation='relu')(temporal_input)
#     temporal_model = MaxPooling3D(pool_size=(1, 2, 2))(temporal_model)
#     temporal_model = Conv3D(128, kernel_size=(3, 3, 3), activation='relu')(temporal_model)
#     temporal_model = MaxPooling3D(pool_size=(1, 2, 2))(temporal_model)
#     temporal_model = Conv3D(256, kernel_size=(3, 3, 3), activation='relu')(temporal_model)
#     temporal_model = Conv3D(256, kernel_size=(3, 3, 3), activation='relu')(temporal_model)
#     temporal_model = MaxPooling3D(pool_size=(1, 2, 2))(temporal_model)
#     temporal_model = Flatten()(temporal_model)
#     temporal_model = Dense(512, activation='relu')(temporal_model)
#     temporal_model = Dropout(0.5)(temporal_model)
#
#     # Merge the two streams
#     merged = keras.layers.concatenate([spatial_model.output, temporal_model])
#
#     # Output layer
#     output = Dense(num_classes, activation='softmax')(merged)
#
#     # Create the model
#     model = Model(inputs=[spatial_model.input, temporal_input], outputs=output)
#
#     return model
#
# # Define the dataset and data generator
# train_data = np.load('path/to/train/data.npy')
# train_labels = np.load('path/to/train/labels.npy')
# test_data = np.load('path/to/test/data.npy')
# test_labels = np.load('path/to/test/labels.npy')
# input_shape = (train_data.shape[1], train_data.shape[2], train_data.shape[3], train_data.shape[4])
# num_classes = 101
# batch_size = 32
#
# def data_generator(data, labels):
#     while True:
#         for i in range(0, data.shape[0], batch_size):
#             x_spatial = data[i:i+batch_size, :, :, :, 0:3]
#             x_temporal = data[i:i+batch_size, :, :, :, 3:6]
#             y = labels[i:i]
