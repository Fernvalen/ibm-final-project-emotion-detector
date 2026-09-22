import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        joy_msg = emotion_detector("I am glad this happened")
        self.assertEqual(joy_msg["dominant_emotion"], "joy")

        anger_msg = emotion_detector("I am really mad about this")
        self.assertEqual(anger_msg["dominant_emotion"], "anger")

        disgust_msg = emotion_detector("I feel disgusted hearing about this")
        self.assertEqual(disgust_msg["dominant_emotion"], "disgust")

        sad_msg = emotion_detector("I am so sad about this")
        self.assertEqual(sad_msg["dominant_emotion"], "sadness")

        fear_msg = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_msg["dominant_emotion"], "fear")

unittest.main()
