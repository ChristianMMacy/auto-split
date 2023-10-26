FROM python:3
LABEL authors="Christian M. Macy <christian@sparrowcompass.com>"

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY model ./model
COPY split.py ./

CMD [ "python", "./split.py" ]
