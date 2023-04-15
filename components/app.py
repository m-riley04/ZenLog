from .logentry import LogEntry
from .emotion import Emotion, COMMON_EMOTIONS
from .day import Day
from .helpers import check_directory
import os
import json

class App:
    def __init__(self):
        self._days = {}
        self.day = None
        
        self.load()
    
    def set_new_day(self):
        '''Sets the new current day'''
        self.day = Day()
        return self.day
    
    def get_date(self):
        '''Returns the date of the current Day'''
        _temp = Day()
        return _temp.date
    
    def save(self):
        '''Saves the current day into the JSON database'''
        # Check for empty day
        if self.day == None:
            return False
        
        currentDate = str(self.get_date())
        self._days[currentDate] = {}
        for key, value in self.day.__dict__.items():
            if type(value) == list:
                _temp = []
                for i in value:
                    _temp.append(i.__dict__)
                value = _temp
                self._days[currentDate][str(key)] = value
            elif type(value) != int and type(value) != bool:
                self._days[currentDate][str(key)] = str(value)
            else:
                self._days[currentDate][str(key)] = value
            
            
        jsonData = json.dumps({"days": self._days}, indent=4)
        
        # Save to file
        _dirPath = f"{os.getcwd()}/user_data"
        print(_dirPath)
        check_directory(_dirPath)
        with open(f"{_dirPath}/days.json", "w") as file:
            file.write(jsonData)
        
    def load(self):
        '''Loads the current day from the database. Returns the day if it finds one, otherwise it create a new one.'''
        # Open JSON data file
        _dirPath = f"{os.getcwd()}/user_data"
        check_directory(_dirPath)
        with open(f"{_dirPath}/days.json", "r") as file:
            self._days = json.loads(file.read())["days"]
        
        # Check every day to see if it matches today
        for day in self._days.keys():
            if day == str(self.get_date()):
                
                # Load day emotions
                for i in self._days[day]["emotions"]:
                    emotions = []
                    emotions.append(Emotion(i["name"], i["severity"]))
                    
                # Load day entries
                for i in self._days[day]["entries"]:
                    entries = []
                    entries.append(LogEntry(i["content"], i["time"]))
                
                # Load day
                self.day = Day(date=day, time=self._days[day]["time"], rating=self._days[day]["rating"], emotions=list(emotions), entries=list(entries), imagePath=self._days[day]["imagePath"], submitted=bool(self._days[day]["submitted"]))
                
                return self.day
        
        # If not, set a new day 
        self.set_new_day()
    
    def add_log_entry(self, text):
        '''Adds a log entry to the entries list'''
        newEntry = LogEntry(content=text)
        self.day.entries.append(newEntry)
        
    def add_emotion(self, emotion):
        '''Adds a new emotion to the emotions list'''
        self.day.emotions.append(emotion)
        
    def create_emotion(self, name, severity=1):
        '''Creates a new emotion object'''
        return Emotion(name=name, severity=severity)
        
    def set_rating(self, rating):
        '''Sets the rating'''
        self.day.rating = rating
        
    def set_emotions(self, emotions):
        '''Sets the emotion list'''
        self.day.emotions = emotions
        
    def set_entries(self, entries):
        '''Sets the log entry list'''
        self.day.entries = entries
        
    def set_imagePath(self, path):
        '''Sets the image path'''
        self.day.imagePath = path
        
    def set_submitted(self, submitted):
        '''Sets the submitted flag'''
        self.day.submitted = submitted
        
    def get_common_emotions(self):
        '''Returns a list of common emotions'''
        return COMMON_EMOTIONS
        
    def get_day(self):
        '''Returns the Day object'''
        return self.day
    
    def get_emotions(self):
        '''Returns the list of emotions'''
        return self.day.emotions
    
    def get_rating(self):
        '''Returns the rating'''
        return self.day.rating
    
    def get_entries(self):
        '''Returns the list of log entries'''
        return self.day.entries
    
    def get_imagePath(self):
        '''Returns the image path'''
        return self.day.imagePath
    
    def get_submitted(self):
        '''Returns the submitted flag'''
        return self.day.submitted