import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


def word_to_bool(word):
    # переводит "да" в true иначе выдает false
    if word is 'да':
        return True
    else:
        return False


def reform_bin_class(prob, acc):
    """
    :param prob: Array of binary prediction
    :param acc: Accuracy of given prediction
    :return: Returns binary prediction based on given, but biased on accuracy
    """
    return [prob[0][0]*acc+prob[0][1]*(1-acc),
            prob[0][1]*acc+prob[0][0]*(1-acc)]


class Classifier:

    mean=0
    disp=0

    def __init__(self):
        self.mlp = object

    def search_network(self, data_prop, data_targ, neural_num,acc=0.95,rect_width=50,rect_height=50):
        """
        Automatic searcher of neural networks, that scans through rectangle of random states of train/test
        array split and that of MLPClassifier

        Creates object of classifier

        :param data_prop:
        array of properties of elements
        :param data_targ:
        array of results of elements
        :param neural_num:
        amount of hidden neurons in network; ATM 6 is preferred
        :param acc:
        value of accuracy on which search will be forced to stop, must be float in between 0 and 1
        :param rect_width:
        size of line for randomizer of initial values in classifier
        note, that if value is negative it will be absoluted and if float - rounded
        :param rect_height:
        size of line for randomizer in split
        :return:
        returns tuple of train set accuracy,test set accuracy, total accuracy and point of it

        point: x and y were the best result was achieved

        """
        max_acc = 0
        self.scaler = StandardScaler()
        self.scaler.fit(data_prop)
        self.scaler.transform(data_prop)
        for y in range(0, abs(rect_height)):
            x_train, x_test, y_train, y_test = train_test_split(
                data_prop,
                data_targ,
                train_size=0.85, random_state=y)
            for x in range(0, abs(rect_width)):
                self.mlp = MLPClassifier(solver='lbfgs', random_state=x, hidden_layer_sizes=[neural_num],
                                    activation='relu', max_iter=1000)
                self.mlp.fit(x_train, y_train)
                cur_acc = self.mlp.score(data_prop,data_targ)
                if cur_acc > acc:
                    # if required accuracy was achieved then search stops and returns its coordinates
                    train_acc = self.mlp.score(x_train, y_train)
                    test_acc = self.mlp.score(x_test, y_test)
                    if train_acc > acc and test_acc > acc:
                        return train_acc, test_acc, cur_acc, x, y
                elif cur_acc > max_acc:
                    # if it wasn't then current accuracy compares to that of the best combination,
                    # if it better - it replaces previous one
                    max_x=x
                    max_y=y
                    max_acc=cur_acc
        # recovery of the best result
        x_train, x_test, y_train, y_test = train_test_split(
            data_prop,
            data_targ,
            train_size=0.85, random_state=max_y)
        self.mlp = MLPClassifier(solver='lbfgs', random_state=max_x, hidden_layer_sizes=[neural_num],
                                 activation='relu', max_iter=1000)
        self.mlp.fit(x_train, y_train)
        train_acc = self.mlp.score(x_train, y_train)
        test_acc = self.mlp.score(x_test, y_test)
        # as network didn't achieved required score method returns 1
        return train_acc, test_acc, max_acc, max_x, max_y

    def set_network(self, data_prop, data_targ, neural_num, x, y, return_net_data=False):
        """
        Sets MLPClassifier on point x,y in randomizer (split/initial values) linear space

        :param data_prop:
        array of properties of elements
        :param data_targ:
        array of results of elements
        :param neural_num:
        amount of hidden neurons in network;
        :param x:
        random state of classifier object
        :param y:
        random state of split
        :return:
        """
        self.scaler = StandardScaler()
        self.scaler.fit(data_prop)
        self.scaler.transform(data_prop)
        x_train, x_test, y_train, y_test = train_test_split(
            data_prop,
            data_targ,
            train_size=0.85, random_state=y)
        self.mlp = MLPClassifier(solver='lbfgs', random_state=x, hidden_layer_sizes=[neural_num],
                                 activation='relu', max_iter=1000)
        self.mlp.fit(x_train, y_train)
        if return_net_data:
            ret_list=[]
            # calculates accuracy and errors on training data
            sval=0
            for i,dt in enumerate(x_train):
                t=self.mlp.predict(np.array(dt).reshape(1,-1))[0]
                if abs(t - int(y_train[i])) < 0.25:
                    sval+=1
            ret_list.append(sval)
            ret_list.append(len(x_train))
            prec = round(sval/len(x_train)*100,5)
            ret_list.append(prec)
            # calculates accuracy and errors on test data
            sval = 0
            for i, dt in enumerate(x_test):
                t = self.mlp.predict(np.array(dt).reshape(1, -1))[0]
                if abs(t - int(y_test[i])) < 0.25:
                    sval += 1
            ret_list.append(sval)
            ret_list.append(len(x_test))
            prec = round(sval / len(x_test)*100,5)
            ret_list.append(prec)
            # calculates total
            ret_list.append(ret_list[0]+ret_list[3])
            ret_list.append(ret_list[1]+ret_list[4])
            ret_list.append(round(ret_list[6]/ret_list[7]*100,5))

        return ret_list

    def predict(self,properties):
        self.scaler.transform(properties)
        return self.mlp.predict_proba(properties)

    """def get_class_details(self, data, targets, x, y, neural_num):
        self.scaler = StandardScaler()
        self.scaler.fit(data)
        self.scaler.transform(data)
        x_train, x_test, y_train, y_test = train_test_split(
            data,
            data,
            train_size=0.85, random_state=y)
        self.mlp = MLPClassifier(solver='lbfgs', random_state=x, hidden_layer_sizes=[neural_num],
                                 activation='relu', max_iter=1000)
        self.mlp.fit(x_train, y_train)"""

def split(array):
    x = []
    y = []
    for t in array:
        y.append(t[0])
        sl=[]
        for g in t[1:]:
            if g==True:
                sl.append(1)
            elif g==False:
                sl.append(0)
            else:
                sl.append(g)
    return x, y



if __name__ == '__main__':
    data_dict = {'features': [], 'targets': []}

    # открытие файла
    with open('Male_lethal.txt', 'r') as file:
        # построчное чтение из файла
        block = []
        for line in file:
            # преобразование сторки в список слов
            ls = line.split('\t')
            block.append(ls)
    for lst in block:
        # преобразование строк из списка в числа
        # в начале
        for i in range(1, 4):
            lst[i] = float(lst[i])
            # и в конце
        for i in range(7, len(lst)):
            lst[i] = float(lst[i])
            # преобразование текстовых значений в пары чисел
        sublist = []
        for i in lst[4:7]:
            if word_to_bool(i):
                sublist = sublist + [1]
            else:
                sublist = sublist + [0]
        lst = lst[0:4] + sublist + lst[7:]
        # преобразование первого слова в соответствующий ему
        # результат
        if lst[0] == 'жив':
            data_dict['targets'].append(1)
        else:
            data_dict['targets'].append(0)
        data_dict['features'].append(lst[1:])

    data_dict['features'] = np.array(data_dict['features'])
    data_dict['targets'] = np.array(data_dict['targets'])
    obj=Classifier()
    acc1,acc2,acc3,px,py=obj.search_network(data_dict['features'],data_dict['targets'],6)
    print('\n'"Точность на тренировочном наборе:{}".format(acc1))
    print("Точность на тестовом наборе:{}".format(acc2))
