def sublists(lst):
    """
    Computes all sublists of the input list.
    Input:
        lst: list of values
    
    Returns: (list of list of values) list of all sublists of lst.
    """

    if lst == []:
        return [[]]
    else:  
        list_of_sublist = []
        val = [lst[0]]
        lst_without_val = lst[1:]
        sublists_without_val = sublists(lst_without_val)
        print(sublists_without_val)
        for sublist in sublists_without_val:
            list_of_sublist.append(sublist)
            true_sublist = val + sublist
            list_of_sublist.append(true_sublist)
        return list_of_sublist

    



#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_sublists(lst):
    original_lst = list(lst)
    recreate_msg = utils.gen_recreate_msg('sublists', original_lst)
    expected = [[x for j, x in enumerate(lst) if i ^ (2 ** j) < i] 
        for i in range(2 ** len(lst))]
    actual = sublists(lst)
    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    for el in actual:
        utils.check_type(el, [], recreate_msg)
    utils.check_equals(sorted(actual), sorted(expected), recreate_msg)
    utils.check_parameter_unmodified(lst, original_lst, "lst", recreate_msg)


def test_sublists_1():
    do_test_sublists(['apple'])

def test_sublists_2():
    do_test_sublists([12])

def test_sublists_3():
    do_test_sublists([True])

def test_sublists_4():
    do_test_sublists(['A', 'B'])

def test_sublists_5():
    do_test_sublists(["apple", "tomato"])

def test_sublists_6():
    do_test_sublists(['A', 'B', 'C'])

def test_sublists_7():
    do_test_sublists([50, 150, 100])

def test_sublists_8():
    do_test_sublists(['A', 'B', 'C', 'D'])

def test_sublists_9():
    do_test_sublists([50, 0, -1, 10])

def test_sublists_10():
    do_test_sublists([50, 0, -1, 10, 5])

def test_sublists_11():
    do_test_sublists(['A', 'B', 'C', 'D', 'E'])

def test_sublists_12():
    do_test_sublists(['U', 'V', 'W', 'X', 'Y', 'Z'])

def test_sublists_13():
    do_test_sublists(['water', 'apple', 'tomato', 'zucchini', 'corn', 'stew'])

def test_sublists_14():
    do_test_sublists(list(range(0, 70, 10)))

def test_sublists_15():
    do_test_sublists(list(range(70, 0, -10)))

def test_sublists_16():
    do_test_sublists(list('estuary'))

def test_sublists_17():
    do_test_sublists([1, 2, 3, 5, 8, 13, 21])

def test_sublists_18():
    do_test_sublists([1, -2, 3, -5, 8, -13, 21])

def test_sublists_19():
    do_test_sublists([8, 6, 7, 5, 3, 0, 9])

def test_sublists_20():
    do_test_sublists([1, 2, 3, 5, 8, 13, 21, 34])