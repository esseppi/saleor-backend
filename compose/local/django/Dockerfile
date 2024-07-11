### Build static assets
FROM node:10 as build-nodejs

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

# Install node_modules
COPY app.json package.json package-lock.json /app/
WORKDIR /app
RUN npm install

# Build static
COPY ./saleor/static /app/saleor/static/
COPY ./templates /app/templates/
#RUN STATIC_URL=${STATIC_URL} npm run build-assets --production \
#  && npm run build-emails --production


### Final image
FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

RUN apk update
RUN apk add cairo-dev libxml2-dev libxslt-dev libxml2 pango g++
RUN apk --update --upgrade add git gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN apk update \
  && apk add \
    libxml2 \
    libssl3 \
    shared-mime-info \
    mailcap \
    libgcc \
    libmagic

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client
  # font related - required by weasyprint
#  && apk add ttf-ubuntu-font-family

# Manually install uvloop for 3.8 compatibility
# See: https://github.com/MagicStack/uvloop/pull/275#issuecomment-542887504
RUN git clone \
	--recursive \
	https://github.com/dmontagu/uvloop.git
WORKDIR /uvloop/

## Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
COPY ./requirements_dev.txt /requirements_dev.txt
RUN pip install sphinxcontrib.applehelp==1.0.2 --no-cache-dir
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir -r /requirements_dev.txt

RUN rm -rf /uvloop/

RUN addgroup -S saleor \
    && adduser -S -G saleor saleor


# Install Python dependencies
RUN pip install pipenv
#COPY Pipfile Pipfile.lock /app/
WORKDIR /app
#RUN pipenv install --system --deploy --dev

COPY . /app
COPY --from=build-nodejs /app/saleor/static /app/saleor/static
#COPY --from=build-nodejs /app/webpack-bundle.json /app/
COPY --from=build-nodejs /app/templates /app/templates


COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown saleor /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown saleor /start

COPY ./compose/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker
RUN chown saleor /start-celeryworker

COPY ./compose/production/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat
RUN chown saleor /start-celerybeat

#COPY initial.json /app/

COPY . /app

RUN chown -R saleor /app

USER saleor

WORKDIR /app

RUN SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input

RUN mkdir -p /app/media /app/static \
  && chown -R saleor:saleor /app/


ENTRYPOINT ["/entrypoint"]
