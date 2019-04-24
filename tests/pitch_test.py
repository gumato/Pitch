import unittest
from models import Pitch
Pitch = pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1234,'Python Must Be Crazy','A thrilling new python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

if __name__== '__main__':
    unittest.main()
