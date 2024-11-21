FROM python:3.9

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


COPY . /app



WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD gunicorn --workers=4 --bind 0.0.0.0:8000 app:app