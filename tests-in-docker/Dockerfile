FROM python:3.8-buster AS BrowserBase

MAINTAINER "Exploratory Testing Academy"
LABEL name="Docker build for Robot Framework Tests with Browser Library"

RUN mkdir /app
WORKDIR /app

#Install Node
RUN \
    echo "deb https://deb.nodesource.com/node_12.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
    wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    apt-get update && \
    apt-get install -yqq nodejs && \
    pip install -U pip && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Install WebKit dependencies
RUN apt-get update && apt-get install -y libwoff1 \
                                         libopus0 \
                                         libwebp6 \
                                         libwebpdemux2 \
                                         libenchant1c2a \
                                         libgudev-1.0-0 \
                                         libsecret-1-0 \
                                         libhyphen0 \
                                         libgdk-pixbuf2.0-0 \
                                         libegl1 \
                                         libnotify4 \
                                         libxslt1.1 \
                                         libevent-2.1-6 \
                                         libgles2 \
                                         libvpx5

# Install gstreamer and plugins to support video playback in WebKit.
RUN apt-get update && apt-get install -y gstreamer1.0-gl \
                                         gstreamer1.0-plugins-base \
                                         gstreamer1.0-plugins-good \
                                         gstreamer1.0-plugins-bad
# Install Chromium dependencies
RUN apt-get update && apt-get install -y libnss3 \
                                         libxss1 \
                                         libasound2 \
                                         fonts-noto-color-emoji
# Install Firefox dependencies
RUN apt-get update && apt-get install -y libdbus-glib-1-2 \
                                         libxt6

# Install ffmpeg to bring in audio and video codecs necessary for playing videos in Firefox.
RUN apt-get update && apt-get install -y ffmpeg

# Add user so we don't need --no-sandbox in Chromium
RUN groupadd -r docker && useradd -r -g docker -G audio,video docker \
    && mkdir -p /home/docker/Downloads \
    && chown -R docker:docker /home/docker

ENV NODE_PATH=/usr/lib/node_modules
ENV PYTHONPATH=/usr/lib/python3

#Initialize Browser Library
RUN rfbrowser init

# Run everything after as non-privileged user
RUN mv /root/.cache/ /home/docker/.cache
RUN chmod a+rwx -R /home/docker/.cache
#workaround for a problem with robotframework-browser
RUN chmod 777 -R /usr/local/lib/python3.8/site-packages/Browser/wrapper/

USER docker

# To run inside docker locally enable one of the below
# ENTRYPOINT ["/app/scripts/entrypoint_perf_test.sh"]
ENTRYPOINT ["/app/scripts/entrypoint_test.sh"]
