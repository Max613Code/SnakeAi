import numpy
from sklearn import svm
import random
import math
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import torch

from sklearn import preprocessing

class ai():
    game = 0
    data = []
    data_result = []
    current_info = [[[],[],[],[],[],[]]]

    num = 0

    # 0 for nothing
    #1 for wall
    #2 for snake
    #3 for food

    array_of_surroundings = []
    w=0.5

    model = None

    SVG=False
    neural=True

    my_model = 0

    def submit_info(self, surrounding, died, move, state):
        #print(surrounding)
        if (died):
            if(random.random()>0.3):
                if len(self.data)>0:
                    self.data.pop()
                    self.data_result.pop()
                return
        if (random.random() > 0.9):
            for j in surrounding:
                for i in j:
                    if (i==3):
                        if len(self.array_of_surroundings) > 3:
                            if (type(move[-1]) is int):
                                self.data.append(self.array_of_surroundings[-1])
                                self.data_result.append(move[-1])
                                if (state=="f"):
                                    self.data.append(self.array_of_surroundings[-1])
                                    self.data_result.append(move[-1])
                                    self.data.append(self.data[-3])
                                    self.data_result.append(self.data_result[-3])
            for i in surrounding:
                for j in i:
                    if (j==1):
                        if len(self.array_of_surroundings) > 3:
                            if (type(move[-1]) is int):
                                self.data.append(self.array_of_surroundings[-1])
                                self.data_result.append(move[-1])

        #with open('data.txt', 'a') as file:
        #    file.write(str(self.data))

    def get_choice(self, surrounding):
        self.array_of_surroundings.append(surrounding)
        #print(self.data)
        #print(self.data_result)
        if (len(self.data) > 3 and len(numpy.unique(self.data_result)) > 1):
            if (random.random() > self.w):
                if (self.SVG):
                    self.model = svm.SVC()
                    ndata = numpy.array(self.data)
                    nsamples, nx, ny = ndata.shape
                    d2_train_dataset = ndata.reshape((nsamples, nx * ny))

                    res_data_n = numpy.array(self.data_result, dtype='object').reshape(-1,1)
                    res_data_n = res_data_n.astype(int)

                    self.model.fit(d2_train_dataset, res_data_n.ravel())

                    ndata = numpy.array([surrounding],dtype='object')
                    nsamples, nx, ny = ndata.shape
                    d2_train_dataset = ndata.reshape((nsamples, nx * ny))

                    prediction =  self.model.predict(d2_train_dataset)
                elif self.neural:
                    first= False
                    ndata = numpy.array(self.data)
                    nsamples, nx, ny = ndata.shape
                    d2_train_dataset = ndata.reshape((nsamples, nx * ny))

                    res_data_n = numpy.array(self.data_result, dtype='object').reshape(-1, 1)
                    res_data_n = res_data_n.astype(int)

                    features = (ndata)
                    labels = (res_data_n.ravel())
                    print(features.shape,labels.shape)

                    features_train, features_test, labels_train, labels_test = train_test_split(features, labels,
                                                                                                test_size=0.2,
                                                                                                random_state=42)
                    if not first:
                        self.my_model = Sequential()
                        input = InputLayer(input_shape=(features.shape[-1]))

                        self.my_model.add(input)

                        self.my_model.add(Dense(4, activation='relu'))
                        self.my_model.add(Dense(4, activation='relu'))
                        # my_model.add(Dense(16, activation='tanh'))
                        # my_model.add(Dense(16, activation='tanh'))

                        self.my_model.add(Dense(1))

                        print(self.my_model.summary())

                        opt = Adam(learning_rate=0.005)

                        callback = tf.keras.callbacks.EarlyStopping(monitor='mae', patience=100, min_delta=1)

                        self.my_model.compile(loss='mse', metrics=['mae'], optimizer=opt)
                        #self.my_model.fit(tf.data.Dataset.from_tensor_slices(features_train), validation_data=tf.data.Dataset.from_tensor_slices(labels_train), epochs=5, batch_size=1, verbose=1,
                                     #callbacks=[callback])
                        self.my_model.fit((features_train), labels_train, validation_data=(features_test, labels_test),
                                          epochs=2, batch_size=1, verbose=1,
                                          callbacks=[callback])
                        first = True
                    elif first:
                        opt = Adam(learning_rate=0.005)

                        callback = tf.keras.callbacks.EarlyStopping(monitor='mae', patience=100, min_delta=1)
                        self.my_model.fit((features_train), labels_train, validation_data=(features_test, labels_test), epochs=2, batch_size=1, verbose=1,
                                     callbacks=[callback])

                    ndata = numpy.array([surrounding], dtype='object')
                    nsamples, nx, ny = ndata.shape
                    d2_train_dataset = ndata.reshape((nsamples, nx * ny))
                    print(d2_train_dataset)
                    d2_train_dataset=numpy.asarray(d2_train_dataset).astype('float32')
                    d2_train_dataset=d2_train_dataset.reshape(6,5)
                    prediction = self.my_model.predict(d2_train_dataset)[0]



            else:
                prediction = random.choice([1,2,3,4])
            print("Trained! " + str(self.game.calculted_fitness()) + " " + str(self.num))
            self.w*=1.5*(1-1/(1+(-1 * math.exp((min(7, (len(self.data))))))))
            #print(self.w)
            self.w = min(5,self.w)
            return prediction
        else:
            return random.choice([1,2,3,4])

    def clean_data(self):
        for i in range(0,len(self.data)-1):
            dat_copy=self.data.clone()
            dat_res_copy=self.data_result.clone()

