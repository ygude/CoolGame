FROM ubuntu:20.04
RUN apt-get update \
        && DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes python3-dev python3-pip python3-jenkins cmake \
        && apt-get autoremove --quiet --yes \
        && apt-get clean --quiet --yes
RUN addgroup --gid 22221 atgjenkins \
    && adduser --home /jenkins --shell /bin/bash --gecos '' --uid 22221 --gid 22221 --disabled-password atgjenkins
USER atgjenkins
