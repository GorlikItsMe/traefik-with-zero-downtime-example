FROM python:3.6-slim

WORKDIR /app

RUN apt update && apt install -y wget
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app.py /app/app.py

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]

HEALTHCHECK  --interval=10s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:5000/health?dockefile || exit 1
