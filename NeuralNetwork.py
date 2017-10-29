import random

class NeuralNetwork:
    """ This class represents neural network which is used
        competitive learning method - winner take all!
     """

    _inputs_count = 0  # number of inputs
    _outputs_counts = 0  # number of output neurons
    _weights = []  # matrix of weight: i - output, j - input

    _study_speed = 0.5 # default: 0.5


    def __init__(self, inputs_count, outputs_count, study_speed = 0.5):
        self._inputs_count = inputs_count
        self._outputs_counts = outputs_count
        self._study_speed = study_speed
        self._init_weights()


    def _init_weights(self):
        """ Init weights with rundom number in range [0, 1] """

        for i in range(self._outputs_counts):
            self._weights.append([])
            for j in range(self._inputs_count):
                self._weights[i].append(random.random())


    def evaluate(self, signals):
        """ Evaluate result of neural network on inputs with signals """

        max_output = self._calculate_sum(signals, self._weights[0])
        max_index = 0

        for i in range(1, self._outputs_counts):
            curr_sum = self._calculate_sum(signals, self._weights[i])
            if curr_sum > max_output:
                max_output = curr_sum
                max_index = i

        # print(max_index)

        return max_index


    # Private methods
    def _calculate_sum(self, signals, weights):
        """ Calculate weighted sum  """

        s = 0
        for i in range(len(signals)):
            s += signals[i] * weights[i]
        return s


    def study(self, signals, answer):
        """ Study neural network with formula: Wij(k + 1) = Wij(k) + r * (Xj - Wij(k)),
            where Wij(k) is the jth weight of the ith output neuron on the kth epoch,
            Xj is a signal on the jth input neuron,
            r is a coefficient of studying speed
         """

        for j in range(self._inputs_count):
            weight = self._weights[answer][j]
            self._weights[answer][j] = weight + self._study_speed * (signals[j] - weight)