# pull official base image
FROM registry.ghaf.cloud/library/django-alpine:V0.0.2

# create the appropriate directories
ENV APP_HOME=/usr/src/app

# copy entrypoint-prod.sh
COPY ./build/entrypoint.sh $APP_HOME

COPY ./requirements/production.txt .
RUN pip install -r production.txt

# copy project
COPY ./src $APP_HOME

# lint
RUN flake8 --ignore=E501,F401 .

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
