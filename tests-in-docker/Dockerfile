FROM mcr.microsoft.com/playwright  AS InstallEnv

MAINTAINER "Exploratory Testing Academy"
LABEL name="Docker build for Robot Framework Tests with Browser Library and Pabot"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENV NODE_PATH=/usr/lib/node_modules
ENV PYTHONPATH=/usr/lib/python3

RUN rfbrowser init

# To run inside docker locally enable one of the below
#ENTRYPOINT ["/app/scripts/entrypoint_perf_test.sh"]
ENTRYPOINT ["/app/scripts/entrypoint_test.sh"]
