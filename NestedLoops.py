import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
times = ["Morning","Evening","Night"]
for day in days:
    day_moods = random.choice(moods)
    for time in times:
        day_moods = random.choice(moods)
        print(f"On {day} {time}, I was felling {day_moods}")

    