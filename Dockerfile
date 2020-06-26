FROM shephexd/python:3.6

WORKDIR /webapp/server/
ADD . /webapp/server/
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
