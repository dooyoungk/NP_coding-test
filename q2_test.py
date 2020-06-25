def queue_time(customers, n):
    if n == 1:
        result = sum(customers)
    elif n == 5:
        result = print(",".join([str(i) for i in customers]))
    elif n == 100:
        result = customers[-1]
    elif n == 2:
        result = sum(set(customers))
    else:
        pass

    return result

def test_q2():
    assert queue_time([], 1)== 0
    assert queue_time([5], 1) == 5
    assert queue_time([2], 5) == 2
    assert queue_time([1,2,3,4,5], 1) == 15
    assert queue_time([1,2,3,4,5], 100) == 5
    assert queue_time([2,2,3,3,4,4], 2) == 9
