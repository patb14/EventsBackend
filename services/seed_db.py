from django import setup
from django.core.management import call_command


# TODO: Create a super user on start - use docker
def seed_db():
    # Need to set up the app before seeding
    setup()
    call_command("loaddata", "./events/testing/seed_data/event_locations.json")
    call_command("loaddata", "./events/testing/seed_data/genders.json")
    call_command("loaddata", "./events/testing/seed_data/levels_of_play.json")
    call_command("loaddata", "./events/testing/seed_data/player_positions.json")
    call_command("loaddata", "./events/testing/seed_data/sessions.json")
    call_command("loaddata", "./events/testing/seed_data/events.json")


if __name__ == "__main__":
    seed_db()
