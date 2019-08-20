FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install -r requirements.txt
# 実行
#CMD ["python", "run.py"]
CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"]
