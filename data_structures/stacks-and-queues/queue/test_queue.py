
def test_enqueue(empty_qu):
    empty_qu.enqueue(8)
    assert empty_qu.back.val == 8


def test_enqueue_1(few_queue):
    few_queue.enqueue(4)
    assert few_queue.front.val == 1
    assert few_queue.back.val == 4


def test_enqueue_2(few_queue):
    few_queue.enqueue(10)
    few_queue.enqueue(7)
    assert few_queue.front.val == 1
    assert few_queue.back.val == 7