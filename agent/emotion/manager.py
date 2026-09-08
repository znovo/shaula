

class EmotionManager:
    def __init__(self):
        self.emotions = {
            "neutral": 1.0,
            "happy": 0.0,
            "sad": 0.0,
            "angry": 0.0,
            "calm": 0.0
        }
        self.opposites = {
            "neutral": None,
            "happy": "sad",
            "sad": "happy",
            "angry": "calm",
            "calm": "angry"
        }
    def set_emotion(self, emotion, intensity):
        if emotion in self.emotions:
            self.emotions[emotion] = intensity
            opposite_emotion = self.opposites.get(emotion)
            if opposite_emotion:
                self.emotions[opposite_emotion] = 1.0 - intensity
        else:
            raise ValueError(f"Emotion '{emotion}' is not recognized.")

    def get_emotion(self, emotion):
        return self.emotions.get(emotion, None)
    
    def get_all_emotions(self):
        return self.emotions

    def get_dominant_emotion(self):
        dominant_emotion = max(self.emotions, key=self.emotions.get)
        return dominant_emotion, self.emotions[dominant_emotion]

    