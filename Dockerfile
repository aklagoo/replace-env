FROM python:3.9.16-slim

COPY entrypoint.py /usr/local/bin/

RUN echo "Hello world!" >> test.txt

RUN chmod +x /usr/local/bin/entrypoint.py

RUN cat test.txt

ENTRYPOINT [ "python3", "/usr/local/bin/entrypoint.py" ]