import unittest
from challenge import ocr_format

class TestChallenge(unittest.TestCase):

    def test_capitalization_of_sentences(self):
        data = 'this is a sentence.  this is another sentence.  '
        solution = 'This is a sentence.  This is another sentence.  '
        self.assertEqual(ocr_format(data), solution)

    def test_separation_of_sentences(self):
        data = 'This is a sentence.This is another sentence.'
        solution = 'This is a sentence.  This is another sentence.  '
        self.assertEqual(ocr_format(data), solution)

    def test_no_space_before_puctuation(self):
        data = 'This is a sentence .  '
        solution = 'This is a sentence.  '
        self.assertEqual(ocr_format(data), solution)

    def test_commas_followed_by_single_space(self):
        data = 'This is a sentence,with a comma.  '
        solution = 'This is a sentence, with a comma.  '
        self.assertEqual(ocr_format(data), solution)

    def test_replacement_of_semicolons(self):
        data = 'This is a sentence;  this is another sentence.  '
        solution = 'This is a sentence.  This is another sentence.  '
        self.assertEqual(ocr_format(data), solution)

    def test_proper_names_capitalization(self):
        data = 'jack and jill went up the hill.  '
        solution = 'Jack and Jill went up the hill.  '
        self.assertEqual(ocr_format(data), solution)

    def test_mixed_cases(self):
        data = 'this is a sentence;this is another sentence,with a comma..  '
        solution = 'This is a sentence.  This is another sentence, with a comma.  '
        self.assertEqual(ocr_format(data), solution)

    def test_extra_spaces(self):
        data = 'This is a sentence.    This is another sentence.  '
        solution = 'This is a sentence.  This is another sentence.  '
        self.assertEqual(ocr_format(data), solution)

    def test_complete_example(self):
        data = 'Jack and jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.He fell down and broke his smartphone.    "Oh dear!" said jack;actually,he didn’t say "Oh dear",he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.jill was so shocked that she didn’t look where she was going and fell down,too, tumbling all the way down the hill;  jack got up and went home to mend his phone.    jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone; Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again .'
        solution = 'Jack and Jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.  He fell down and broke his smartphone.  "Oh dear!" said Jack.  Actually, he didn’t say "Oh dear", he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.  Jill was so shocked that she didn’t look where she was going and fell down, too, tumbling all the way down the hill.  Jack got up and went home to mend his phone.  Jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone.  Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again.  '
        self.assertEqual(ocr_format(data), solution)

if __name__ == '__main__':
    unittest.main()