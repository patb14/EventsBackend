FROM python:3.10-alpine

RUN python -m pip install --upgrade pip

# Prevent .pyc files from being written
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
# Set the python path so docker can see the modules
ENV PYTHONPATH "${PYTHONPATH}:/services"

ENV DJANGO_SETTINGS_MODULE=services.settings

# Install the requirements
WORKDIR /services
COPY requirements.txt /services/
RUN pip install -r requirements.txt

COPY . /services/