from datetime import time, datetime, date, timedelta

from model.File import File


def format_time(delta: timedelta):
    return (datetime.utcfromtimestamp(0) + delta).strftime("%H:%M:%S.%f")[:-5]


class OutputFile(File):
    default_duration = '00:00:00.000'

    start = default_duration
    end = default_duration
    duration = default_duration

    def __init__(self, file):
        super().__init__(file)
        try:
            self.start = time.fromisoformat(file.get("start", self.start))
            self.end = time.fromisoformat(file.get("end", self.end))

            delta = datetime.combine(date.min, self.end) - datetime.combine(date.min, self.start)
            self.duration = file.get("duration", format_time(delta))
        except ValueError as e:
            print(f'''There was a problem reading the time values for {self.name}
Time values must be specified as "00:00:00(.000)" (Hours:Minutes:Seconds(.OptionalMilliseconds))''')
            raise e
