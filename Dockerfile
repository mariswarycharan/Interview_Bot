FROM  python:3.10
WORKDIR  /app
COPY  .  /app
RUN  pip  install  --trusted-host  pypi.python.org  -r  requirements.txt
EXPOSE  80
CMD  ["python",  "app.py"]