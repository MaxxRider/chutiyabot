FROM python:3.7-slim AS builder
WORKDIR /opt

RUN apt -qq update && apt -qq install -y git gcc gnupg

ENV VIRTUAL_ENV=/opt/venv
RUN pip3 install --ignore-installed distlib pipenv && \
    python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /opt/
RUN pip3 install --no-cache-dir -r requirements.txt


FROM python:3.7-slim AS production
WORKDIR /opt

COPY setup.sh /tmp/setup.sh
COPY download.conf /opt/
RUN bash /tmp/setup.sh

ENV VIRTUAL_ENV=/opt/venv
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . .
CMD ["python3", "-m", "robote"]
