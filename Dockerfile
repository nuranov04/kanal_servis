FROM python:3.8


RUN mkdir -p /project/
RUN pwd

WORKDIR /project/
COPY . /project/
RUN pip install --upgrade pip
RUN pip install -r req.txt
EXPOSE 8000
CMD [ "python", "app.py" ]
