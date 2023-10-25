# Use most lightweight base image possible
FROM alpine:latest

# Install required packages for app to run
RUN apk add --no-cache git ffmpeg python3 py3-pip
#RUN apk add --no-cache git python3 py3-pip

# Make app dir
WORKDIR /app

# Copy source files
ADD . /app

# Install Python dependencies using pip (if there will be any)
#RUN pip install -r requirements.txt

# Install Python dependencies using pip (hardcoded)
RUN pip install ffmpeg python-ffmpeg pyyaml

# Clear unwanted files and cleanup
RUN apk del git \
    && rm -rf /var/cache/apk/* \
    && rm -rf /root/.cache \
    && rm -rf /app/.git

# Set the default command to run your application (you have to mount video and yaml into /app/resources)
CMD ["python3", "split.py"]
