import sys
import subprocess
import time
import os

from samegame import *
from search import *
from utils import *

TESTS_FOLDER = 'tests/'

passed = 0
failed = 0
    
def xx_recursive_sort(lst):
    """ Function needed to run some of the tests, that orders the groups
    according to a criteria. This is not the function used in evalutiation
    but it seems to output the same result. """
    for el in lst:
        el.sort()
    return lst
    
def getTests():
    """ Checks tests directory for existing tests. If you wish you may
    add more tests, as long as it has all the necessary files """
    tests = next(os.walk(TESTS_FOLDER))[1]
    tests.sort()
    return tests

if __name__ == '__main__':
    
    orig_stdout = sys.stdout
    tests = getTests()
    
    for test in tests:
        print('\n>> Executing ' + test)
        
        inputFile = TESTS_FOLDER + test + '/input'
        outputFile = TESTS_FOLDER + test + '/output'
        resultFile = TESTS_FOLDER + test + '/result'
        diffFile = TESTS_FOLDER + test + '/diff.txt'
        
        with open(inputFile) as i:
            code = i.read()
        
        r = open(resultFile, 'w')
        
        # Redirect print() to result file
        sys.stdout = r
        
        try:
            eval(code)
            r.close()
        except Exception as e:
            sys.stdout = orig_stdout
            print('[ERROR] ' + test + ' does not run due to error:')
            print(e.args[0])
            failed += 1
            r.close()
            continue
        
        sys.stdout = orig_stdout
        time.sleep(0.1)
        
        diffs = ''
        
        try:
            subprocess.check_output(['diff', resultFile, outputFile])
        except subprocess.CalledProcessError as e:
            # Since diffs are printed to stderr, whe need to catch them here
            diffs = e.output.decode('utf-8')
        
        if diffs:
            print('Test failed! Check details in diff file.\n' + diffs + '\n')
            r = open(diffFile, 'w')
            r.write(diffs)
            r.close()
            failed += 1
        else:
            print('Test passed!')
            passed += 1
            
    print('\nTESTS PASSED: ' + str(passed))
    print('TESTS FAILED: ' + str(failed) + '\n')
