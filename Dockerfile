FROM python:3.11.6-alpine3.18 AS build-stage
LABEL maintainer="Andreas Violaris"
COPY app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.6-alpine3.18
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
COPY --from=build-stage $PYTHONPATH $PYTHONPATH
COPY --from=build-stage /app /app
WORKDIR /app
HEALTHCHECK --interval=12s --timeout=12s --start-period=30s CMD python3 healthcheck.py
ENTRYPOINT ["python3", "app.py"]