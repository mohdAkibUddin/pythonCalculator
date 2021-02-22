FROM python:latest

ADD . .

CMD ["python", "-m", "unittest", "discover", "-s","tests"]