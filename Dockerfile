FROM python:3.10

COPY . .

RUN make deps