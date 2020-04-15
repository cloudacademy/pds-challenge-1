import string
data = 'Jack and jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.He fell down and broke his smartphone.    "Oh dear!" said jack;actually,he didn’t say "Oh dear",he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.jill was so shocked that she didn’t look where she was going and fell down,too, tumbling all the way down the hill;  jack got up and went home to mend his phone.    jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone; Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again .'
# ====================================
# Do not change the code before this

## Add your functions here



# ====================================
# Do not change the code after this

def ocr_format(text):
    '''
    Return a string containing the text formatted as follows:
    - Sentences must start with a capital letter.
    - Sentences must be separated by two spaces.
    - Commas must be followed by a single space.
    - Semi-colons must be replaced with full stops.
    - Duplicate punctuation must be removed.

    Hint: You will need to write a lookup list into your code 
          so that you can check for proper names and ensure that 
          they are capitalised appropriately.

    Arguments
    text: a string of text received from the OCR

    Examples 
    ocr_format(data) returns the following formatted string
    "Jack and Jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.  He fell down and broke his smartphone.  "Oh dear!" said Jack.  Actually, he didn’t say "Oh dear", he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.  Jill was so shocked that she didn’t look where she was going and fell down, too, tumbling all the way down the hill.  Jack got up and went home to mend his phone.  Jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone.  Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again. "
    '''
    # ====================================
    # Do not change the code before this


    


if __name__ == '__main__':
    print(ocr_format(data))
