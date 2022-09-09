FROM python:3.9

WORKDIR /app
COPY requirements.txt requirements.txt
COPY runner.sh runner.sh
RUN pip3 install -r requirements.txt

EXPOSE 5000

# RUN python -m venv venv
# RUN source venv/bin/activate

CMD  "./runner.sh"



