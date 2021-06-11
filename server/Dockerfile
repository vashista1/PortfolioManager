FROM python:3
WORKDIR /usr/src/server/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "run.py" ]
