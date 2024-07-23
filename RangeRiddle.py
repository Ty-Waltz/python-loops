import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for day in days:
    day_moods = random.choice(moods)
    print(f"On day {day} I was feeling {day_moods}!")
    
