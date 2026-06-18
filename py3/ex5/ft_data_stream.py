import typing
import random


def player_list() -> list[str]:
    return ["bob", "dylan", "alice", "charlie"]


def action_list() -> list[str]:
    return ["run", "eat", "sleep", "grab", "move",
            "climb", "sleep", "swim", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = player_list()
    actions = action_list()

    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(events: list[tuple[str, str]]) ->\
        typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        random_index = random.randrange(len(events))
        yield events.pop(random_index)


print("=== Game Data Stream Processor ===")

event_generator = gen_event()

for index in range(1000):
    name, action = next(event_generator)
    print(f"Event {index}: Player {name} did action {action}")

event_list = []
event_generator = gen_event()

for _ in range(10):
    event_list.append(next(event_generator))

print("Built list of 10 events:", event_list)

for event in consume_event(event_list):
    print("Got event from list:", event)
    print("Remains in list:", event_list)
