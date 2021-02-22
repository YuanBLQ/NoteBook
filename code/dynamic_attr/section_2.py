import json

DB_NAME = 'data/schedule_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    with open("example.json", encoding='UTF-8') as fp:
        feed_data = json.load(fp)

    for record_type, rec_list in feed_data["Schedule"].items():
        for record in rec_list:
            key = f"{record_type}.{record['serial']}"
            record['serial'] = key
            db[key] = Record(**record)
