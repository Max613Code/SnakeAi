import numpy
from sklearn import svm
import random
import math

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

    def submit_info(self, surrounding, died, move):
        #print(surrounding)
        if (random.random() > 0.75):
            for j in surrounding:
                for i in j:
                    if (i==3):
                        if len(self.array_of_surroundings) > 3:
                            self.data.append(self.array_of_surroundings[-1])
                            self.data_result.append(move[-1])
            for i in surrounding:
                for j in i:
                    if (j==1):
                        if len(self.array_of_surroundings) > 3:
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
                self.model = svm.SVC()
                ndata = numpy.array(self.data)
                nsamples, nx, ny = ndata.shape
                d2_train_dataset = ndata.reshape((nsamples, nx * ny))

                res_data_n = numpy.array(self.data_result).reshape(-1,1)
                res_data_n = res_data_n.astype(int)

                self.model.fit(d2_train_dataset, res_data_n.ravel())


                ndata = numpy.array([surrounding])
                nsamples, nx, ny = ndata.shape
                d2_train_dataset = ndata.reshape((nsamples, nx * ny))

                prediction =  self.model.predict(d2_train_dataset)
            else:
                prediction = random.choice([1,2,3,4])
            print("Trained! " + str(self.game.calculted_fitness()) + " " + str(self.num))
            self.w*=1.5*(1-1/(1+(-1 * math.exp((min(7, (len(self.data))))))))
            #print(self.w)
            self.w = min(5,self.w)
            return prediction
        else:
            return random.choice([1,2,3,4])