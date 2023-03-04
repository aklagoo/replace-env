FROM python:3.9.16-slim

COPY entrypoint.py /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint.py

ENTRYPOINT [ "python3", "/usr/local/bin/entrypoint.py" ]