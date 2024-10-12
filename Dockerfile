ARG PYTHON_VERSION=3.12
FROM alpine:3.20.1 AS build-stage
ARG PYTHON_VERSION
COPY . /app/instaunfollowers/
RUN apk add --no-cache python3~=${PYTHON_VERSION} py3-pip
WORKDIR /usr/lib/python${PYTHON_VERSION}
RUN python3 -m compileall -o 2 . \
    && find . -name "*.cpython-*.opt-2.pyc" \
    | awk '{print $1, $1}' \
    | sed 's/__pycache__\///2' \
    | sed 's/.cpython-[0-9]\{2,\}.opt-2//2' \
    | xargs -n 2 mv \
    && find . -name "*.py" -delete \
    && find . -name "__pycache__" -exec rm -r {} +
WORKDIR /app/instaunfollowers/
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

FROM alpine:3.20.1
LABEL maintainer="Andreas Violaris"
LABEL description="Dockerfile for InstaUnFollowers application"
LABEL license="CC BY-NC-ND 4.0"
LABEL url="https://hub.docker.com/r/aviolaris/instaunfollowers"
LABEL vcs-url="https://github.com/aviolaris/instaunfollowers"
LABEL documentation_en="https://github.com/aviolaris/instaunfollowers/blob/main/README.md"
LABEL documentation_gr="https://github.com/aviolaris/instaunfollowers/blob/main/README.gr.md"
ARG PYTHON_VERSION
COPY --from=build-stage /usr/bin/python3 /usr/bin/python3
COPY --from=build-stage \
    /usr/lib/libpython${PYTHON_VERSION}.so.1.0 \
    /usr/lib/libpython${PYTHON_VERSION}.so.1.0
COPY --from=build-stage \
    /usr/lib/python${PYTHON_VERSION}/ \
    /usr/lib/python${PYTHON_VERSION}/
COPY --from=build-stage \
    /app/instaunfollowers/ \
    /app/instaunfollowers/
RUN cp -r /app/instaunfollowers/venv/lib/python${PYTHON_VERSION}/site-packages/* \
    /usr/lib/python${PYTHON_VERSION}/site-packages/ \
    && rm -rf /app/instaunfollowers/venv/
WORKDIR /app/instaunfollowers
HEALTHCHECK --interval=12s --timeout=12s --start-period=30s \
    CMD python3 app/healthcheck.py
ENTRYPOINT ["python3", "-m", "app.app"]