import numpy
from sklearn import svm
import random

class ai():
    game = 0
    data = []
    data_result = []
    current_info = [[[],[],[],[],[],[]]]

    # 0 for nothing
    #1 for wall
    #2 for snake
    #3 for food

    array_of_surroundings = []

    model = None

    def submit_info(self, surrounding, food, died, move):
        if food:
            print("q")
            for i in range(3):
                if len(self.array_of_surroundings) > 3:
                    self.data.append(self.array_of_surroundings[-1-i])
                    self.data_result.append(move[-1-i])
        if not died:
            for i in surrounding:
                for j in i:
                    if (j==1):
                        print("h")
                        if len(self.array_of_surroundings) > 3:
                            self.data.append(self.array_of_surroundings[-1 - j])
                            self.data_result.append(move[-1 - j])

        with open('data.txt', 'w') as file:
            file.write(str(self.data))

    def get_choice(self, surrounding):
        self.array_of_surroundings.append(surrounding)
        print("j")
        print(self.data)
        print(self.data_result)
        if (len(self.data) > 3 and len(numpy.unique(self.data_result)) > 1):
            self.model = svm.SVC()
            ndata = numpy.array(self.data)
            nsamples, nx, ny = ndata.shape
            d2_train_dataset = ndata.reshape((nsamples, nx * ny))

            res_data_n = numpy.array(self.data_result).reshape(-1,1)
            res_data_n = res_data_n.astype(int)

            self.model.fit(d2_train_dataset, res_data_n)

            ndata = numpy.array([surrounding])
            nsamples, nx, ny = ndata.shape
            d2_train_dataset = ndata.reshape((nsamples, nx * ny))

            prediction =  self.model.predict(d2_train_dataset)

            return prediction
        else:
            return random.choice([1,2,3])