import numpy as np


def top_result(outputs, ref_q):
    first_ind = np.argmax(outputs, axis=1)
    # first_score =

    first_code = []
    first_q = []
    for i in range(len(first_ind)):
        first_q.append(ref_q[first_ind[i], 0])
        first_code.append(ref_q[first_ind[i], 1])

    return first_ind, first_q, first_code


def second_result(outputs, ref_q, first_ind):
    mask = outputs
    for i in range(len(mask)):
        outputs[i, first_ind[i]] = 0

    # second_ind, second_q, second_code = top_result(outputs, ref_q)

    # second_ind = np.argmax(mask, axis=1)
    #
    # second_code = []
    # second_q = []
    # for i in range(len(second_ind)):
    #     second_q.append(ref_q[second_ind[i], 0])
    #     second_code.append(ref_q[second_ind[i], 1])

    return outputs #second_ind, second_q, second_code
