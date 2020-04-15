import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge")

from challenge import ocr_format

data = 'Jack and jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.He fell down and broke his smartphone.    "Oh dear!" said jack;actually,he didn’t say "Oh dear",he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.jill was so shocked that she didn’t look where she was going and fell down,too, tumbling all the way down the hill;  jack got up and went home to mend his phone.    jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone; Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again .' 
solution = 'Jack and Jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.  He fell down and broke his smartphone.  "Oh dear!" said Jack.  Actually, he didn’t say "Oh dear", he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.  Jill was so shocked that she didn’t look where she was going and fell down, too, tumbling all the way down the hill.  Jack got up and went home to mend his phone.  Jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone.  Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again.  '
class TestChallenge(unittest.TestCase):

    def test(self):
        self.assertEqual(ocr_format(data), solution)


if __name__ == '__main__':
    unittest.main()
