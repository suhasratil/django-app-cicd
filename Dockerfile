FROM python:3.11.12

ENV dockerHOME=/home/app
RUN mkdir -p $dockerHOME
WORKDIR $dockerHOME

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt $dockerHOME
RUN pip install --no-cache-dir -r requirements.txt

COPY . $dockerHOME

WORKDIR $dockerHOME/piston

RUN pip install -r ../requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]