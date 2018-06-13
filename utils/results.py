import numpy as np


def top_result(outputs, ref_q):
    first_ind = np.argmax(outputs, axis=1)
    first_score = np.zeros((10,1))

    for ind in range(len(first_ind)):
        first_score[ind] = outputs[ind, first_ind[ind]]

    first_code = []
    first_q = []
    for i in range(len(first_ind)):
        first_q.append(ref_q[first_ind[i], 0])
        first_code.append(ref_q[first_ind[i], 1])

    return first_ind, first_q, first_code, first_score


def second_result(outputs, ref_q, first_ind):
    mask = outputs
    for i in range(len(mask)):
        mask[i, first_ind[i]] = 0

    second_ind, second_q, second_code, second_score = top_result(mask, ref_q)

    return second_ind, second_q, second_code, second_score
