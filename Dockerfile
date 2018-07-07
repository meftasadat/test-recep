############################################################
# Dockerfile for building test-recep
############################################################

# Set the base image to python:latest
FROM python:3

# File Author / Maintainer
MAINTAINER Mefta Sadat

# Update the repository sources list
RUN apt-get update

# Install dependencies
RUN mkdir -p /opt/cognitive/build/
COPY requirements.txt /opt/cognitive/build/requirements.txt
RUN pip install -r /opt/cognitive/build/requirements.txt
