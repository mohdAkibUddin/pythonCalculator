FROM python:3.8

ADD . .

CMD ["python", "-m", "unittest", "discover", "-s","tests"]