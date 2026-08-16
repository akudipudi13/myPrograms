import unittest

allScores = []

def calc_stat(score: int):
            if score >= 60:
                return "PASS"
            else:
                return "FAIL"

def process_scores(name, score):
    allScores.append(int(score))
    average = sum(allScores) / len(allScores) 
    with open("REPORT.txt", "a") as report:
         report.write(f"{name}, {int(score)}: {calc_stat(int(score))}\n")
    return average
      
        

with open("/Users/akhil/git_repos/myPrograms/scoreCheck/scores.txt", "r") as file:
    for line in file:
        name,score = line.strip().split(",")
        calc_stat(int(score))
        process_scores(name, score)

        
        
class TestCalc(unittest.TestCase):
    def test_score_pass(self):
        self.assertEqual(calc_stat(95), "PASS")

    def test_score_fail(self):
        self.assertEqual(calc_stat(42), "FAIL")

    def test_score_equal(self):
        self.assertEqual(calc_stat(60), "PASS")

    def test_score_zero(self):
        self.assertEqual(calc_stat(0), "FAIL")
    
    
if __name__ == '__main__':
    unittest.main()