from src.day04.Log import Log


def task2(g):
    guards = list(map(lambda x: x[2], g))
    data = list(
        map(lambda x: (x.number, x.most_frequent_sleep_minute, x.minutes[x.most_frequent_sleep_minute]), guards))
    data.sort(key=lambda x: x[2], reverse=True)
    return data[0][0] * data[0][1]


log = Log("day04.input.txt")
guards = list(map(lambda x: (x, log.guards[x].minutes_asleep, log.guards[x]), log.guards.keys()))
guards.sort(key=lambda x: x[1], reverse=True)
sleepy_guard = guards[0]
print("Most sleepy guard " + str(sleepy_guard[0]) + " slept " + str(sleepy_guard[1]) + " minutes")
print("most_frequent_sleep_minute:", sleepy_guard[2].most_frequent_sleep_minute)
print("Answer 1: ", sleepy_guard[0] * sleepy_guard[2].most_frequent_sleep_minute)

print("Answer 2: ", task2(guards))

# print(guards)
