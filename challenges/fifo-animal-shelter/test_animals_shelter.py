from fifo_animal_shelter import AnimalShelter as animal
import pytest

@pytest.fixture
def empty_dog_q():
    return animal()


@pytest.fixture
def dog_q():
    return animal(['dog', 'dog', 'dog', 'dog', 'dog'])


@pytest.fixture
def cat_q():
    return animal(['cat', 'cat', 'cat', 'cat', 'cat', 'cat'])


@pytest.fixture
def mix_q():
    return animal(['cat', 'dog', 'cat',
                   'dog', 'cat', 'cat', 'dog', 'cat', 'dog'])


def test_contsructor():
    ne = animal()
    assert ne.newest is None
    assert ne.oldest is None


def test_enqueue(dog_q):
    dog_q.enqueue('cat')
    assert dog_q.newest.val == 'cat'
    assert dog_q._len == 6


def test_empty_dog_q(empty_dog_q):
    empty_dog_q.enqueue('cat')
    assert empty_dog_q._len == 1
    assert empty_dog_q.newest.val and empty_dog_q.oldest.val == 'cat'


def test_dequeue(empty_dog_q):
    assert empty_dog_q.dequeue() is False