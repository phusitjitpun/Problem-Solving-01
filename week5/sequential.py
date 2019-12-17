import timeit
def sequential():
    for i in number:
        if i == 37:
            return True
number = 1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59
print("Result: ", sequential())

def sequential_time():
    SETUP_CODE = '''
from __main__ import sequential
'''
    TEST_CODE = '''
a = 1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59
sequential()
'''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
    print(times)
    print('Sequential time: {}' .format(min(times)))

if __name__ == "__main__":
    sequential_time()