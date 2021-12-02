import random

DRILLS = [
    'Code out a mergesort algorithm, test with the following examples: [10,3,9,23,1,3,71,2,8,21,60,34]',
    'Code out a quicksort algorithm, test with the following examples: [10,3,9,23,1,3,71,2,8,21,60,34]',
    'How do you create a min-heap from a list? Demonstrate Creation, Insertion, Removal, Peeking. What are the time complexities of each?',
    'How do you create a max-heap from a list? Demonstrate Creation, Insertion, Removal, Peeking. What are the time complexities of each?',


]


def generate_daily_drills(num_of_questions):
    random.shuffle(DRILLS)

    for i in range(num_of_questions):
        print(f"{DRILLS[i]}")


generate_daily_drills(2)
