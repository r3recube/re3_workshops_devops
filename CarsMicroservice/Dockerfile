FROM amazonlinux:2023

WORKDIR /var/tmp
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py --user

WORKDIR /src
COPY src/requirements.txt /src
COPY src/webservice.py /src/
RUN ~/.local/bin/pip3 install -r requirements.txt

CMD ["python3", "webservice.py"]