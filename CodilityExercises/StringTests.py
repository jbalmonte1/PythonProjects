import unittest

from FibFrog import solution

minN = 0
maxN = 100000
minVal = 0
maxVal = 200000

validInput = {
        'validMinValMinLen': {
            'input': [minVal],
            'output': 0,
            },
        'betweenMinMaxValMinLen': {
            'input': [10000],
            'output': 0,
            },
        'validMaxValMinLen': {
            'input': [maxVal],
            'output': 0,
            },
        'validMinValAveLen': {
            'input': [minVal, minVal],
            'output': 0,
            },
        'betweenMinMaxValAveLen': {
            'input': [100, 300, 300],
            'output': 200,
            },
        'validMaxValAveLen': {
            'input': [maxVal, 0],
            'output': 0,
            },
        'validMinValMaxLen': {
            'input': [0]*(maxN-1)+[minVal],
            'output': 0,
            },
        'betweenMinMaxValMaxLen': {
            'input': list(range(minVal, maxN+1)),
            'output': maxN,
            },
        'validMaxValMaxLen': {
            'input': [maxVal]*(maxN),
            'output': 0,
            },
        'duplicates': {
            'input': [maxVal, maxVal],
            'output': 0,
            }
    }

invalidInput = {
        'valLessThanMin': {
            'input': [0, 0],
            'output': 0,
            },
        'valGreaterThanMax': {
            'input': [0, 0],
            'output': 0,
            },
        'negativeVal': {
            'input': [-1],
            'output': 0,
            },
        'zeroVal': {
            'input': [0, 0, 0],
            'output': 1,
            },
        'typeError': {
            'input': ['test'],
            'output': 0,
            },
        'nullVal': {
            'input': ['', 0],
            'output': 0,
            },
        'lenLessThanMin': {
            'input': [0],
            'output': 0,
            },
        'lenGreaterThanMax': {
            'input': [0, 0, 0],
            'output': 0, 
            },
        'lenEqualToZero': {
            'input': [],
            'output': 0,
            }
    }

class StringTests(unittest.TestCase):
    
    #valid
    def testvalidMinValMinLen(self):
        self.assertEqual(solution(validInput['validMinValMinLen']['input']), validInput['validMinValMinLen']['output'])
        
    def testbetweenMinMaxValMinLen(self):
        self.assertEqual(solution(validInput['betweenMinMaxValMinLen']['input']), validInput['betweenMinMaxValMinLen']['output'])
        
    def testvalidMaxValMinLen(self):
        self.assertEqual(solution(validInput['validMaxValMinLen']['input']), validInput['validMaxValMinLen']['output'])

    def testvalidMinValAveLen(self):
        self.assertEqual(solution(validInput['validMinValAveLen']['input']), validInput['validMinValAveLen']['output'])

    def testbetweenMinMaxValAveLen(self):
        self.assertEqual(solution(validInput['betweenMinMaxValAveLen']['input']), validInput['betweenMinMaxValAveLen']['output'])

    def testvalidMaxValAveLen(self):
        self.assertEqual(solution(validInput['validMaxValAveLen']['input']), validInput['validMaxValAveLen']['output'])
        
    def testvalidMinValMaxLen(self):
        self.assertEqual(solution(validInput['validMinValMaxLen']['input']), validInput['validMinValMaxLen']['output'])
        
    def testbetweenMinMaxValMaxLen(self):
        self.assertEqual(solution(validInput['betweenMinMaxValMaxLen']['input']), validInput['betweenMinMaxValMaxLen']['output'])
        
    def testvalidMaxValMaxLen(self):
        self.assertEqual(solution(validInput['validMaxValMaxLen']['input']), validInput['validMaxValMaxLen']['output'])
        
    def testduplicates(self):
        self.assertEqual(solution(validInput['duplicates']['input']), validInput['duplicates']['output'])
        
    #invalid
#===============================================================================
#     def testvalLessThanMin(self):
#         self.assertEqual(solution(invalidInput['valLessThanMin']['input']), invalidInput['valLessThanMin']['output'])
#         
#     def testvalGreaterThanMax(self):
#         self.assertEqual(solution(invalidInput['valGreaterThanMax']['input']), invalidInput['valGreaterThanMax']['output'])
# 
#     def testnegativeVal(self):
#         self.assertEqual(solution(invalidInput['negativeVal']['input']), invalidInput['negativeVal']['output'])
#===============================================================================
        
#===============================================================================
#     def testzeroVal(self):
#         self.assertEqual(solution(invalidInput['zeroVal']['input']), invalidInput['zeroVal']['output'])
# 
#     def testtypeError(self):
#         self.assertEqual(solution(invalidInput['typeError']['input']), invalidInput['typeError']['output'])
#          
#     def testnullVal(self):
#         self.assertEqual(solution(invalidInput['nullVal']['input']), invalidInput['nullVal']['output'])
#          
#     def testlenLessThanMin(self):
#         self.assertEqual(solution(invalidInput['lenLessThanMin']['input']), invalidInput['lenLessThanMin']['output'])
#          
#     def testlenGreaterThanMax(self):
#         self.assertEqual(solution(invalidInput['lenGreaterThanMax']['input']), invalidInput['lenGreaterThanMax']['output'])
#===============================================================================
         
    def testlenEqualToZero(self):
        self.assertEqual(solution(invalidInput['lenEqualToZero']['input']), invalidInput['lenEqualToZero']['output'])

