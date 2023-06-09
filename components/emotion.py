class Emotion:
    def __init__(self, name, severity=1):
        self.name = name
        self.severity = severity
    
    def __str__(self):
        return str(self.name)
    
    def __repr__(self):
        return f"Emotion(name='{self.name}', severity={self.severity})"
    
    def __eq__(self, other):
        if isinstance(other, Emotion):
            return other == self
        else:
            return other == self.name
    
    def __ne__(self, other):
        if isinstance(other, Emotion):
            return other != self
        else:
            return other != self.name
    
#----------------------------------------------------------------
COMMON_EMOTIONS = [
    Emotion("Sadness")
]