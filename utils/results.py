import numpy as np

# Determine index, score, code, and question for most relevant Reference Question
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


# Determine index, score, code, and question for second most relevant Reference Question
def second_result(outputs, ref_q, first_ind):
    mask = outputs
    for i in range(len(mask)):
        mask[i, first_ind[i]] = 0

    second_ind, second_q, second_code, second_score = top_result(mask, ref_q)

    return second_ind, second_q, second_code, second_score


# Display Reference Question, Codes, Score on screen
def display_results(test_probs, test_inputs, ref_q):

    first_ind, first_q, first_code, first_score = top_result(test_probs, ref_q)
    second_ind, second_q, second_code, second_score = second_result(test_probs, ref_q, first_ind)

    print('\n\n')
    for i in range(len(test_inputs)):
        print('Question #%d: %s' % (i+1, test_inputs[i]))
        print('Primary Reference Question: %s' % first_q[i])
        print('Primary Reference Question Code: %s' % first_code[i])
        print('Relevance: %0.3f%%' % (first_score[i]*100))

        print('Secondary Reference Question: %s' % second_q[i])
        print('Secondary Reference Question Code: %s' % second_code[i])
        print('Relevance: %0.3f%%' % (second_score[i]*100))

        print('\n')

    return
