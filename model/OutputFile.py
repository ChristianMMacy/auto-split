import datetime

from model.File import File


def format_time(delta: datetime.timedelta):
    return (datetime.datetime.utcfromtimestamp(0) + delta).strftime("%H:%M:%S.%f")[:-5]


class OutputFile(File):
    title = None
    description = None
    default_duration = '00:00:00.000'

    start = default_duration
    end = default_duration
    duration = default_duration

    def __init__(self, file):
        super().__init__(file)
        self.title = file.get("meta").get("title")
        self.description = file.get("meta").get("description")
        try:
            self.start = datetime.time.fromisoformat(file.get("start", self.start))
            self.end = datetime.time.fromisoformat(file.get("end", self.end))

            delta = datetime.datetime.combine(datetime.date.min, self.end) - datetime.datetime.combine(datetime.date.min, self.start)
            self.duration = file.get("duration", format_time(delta))
        except ValueError as e:
            print(f'''There was a problem reading the time values for {self.name}
Time values must be specified as "00:00:00(.000)" (Hours:Minutes:Seconds(.OptionalMilliseconds))''')
            raise e
