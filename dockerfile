FROM python:3.8.5-slim
RUN pip install pipenv
ADD Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY src ./src
EXPOSE 7777:7777
CMD waitress-serve src.server.server:server
