FROM python:3


WORKDIR /authzpoc
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /authzpoc/src
RUN python setup.py develop

#CMD [ "python", "./your-daemon-or-script.py" ]