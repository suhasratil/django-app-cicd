FROM python:3.11-slim AS builder

ENV appHome=/home/app
ENV buildHome=/home/build

WORKDIR $buildHome

RUN apt-get update && apt-get install -y gcc libpq-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH=/install/lib/python3.11/site-packages
ENV PATH=/install/bin:$PATH

COPY --from=builder /install /install

COPY . .

WORKDIR $appHome/piston

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]