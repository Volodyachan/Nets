FROM python:3.8

RUN apt-get update
RUN apt-get install --yes iputils-ping

WORKDIR /mtu_solution

COPY mtu_solution.py /mtu_solution/
ENTRYPOINT ["python3", "/mtu_solution/mtu_solution.py"]