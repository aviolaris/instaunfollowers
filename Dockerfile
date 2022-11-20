FROM python:3.10-slim AS build-stage
LABEL maintainer="Andreas Violaris"
COPY app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3
ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages
COPY --from=build-stage $PYTHONPATH $PYTHONPATH
COPY --from=build-stage /app /app
WORKDIR /app
ENTRYPOINT ["python3", "app.py"]