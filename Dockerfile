FROM rust:1.86-bookworm AS builder

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3 \
        python3-dev \
        python3-venv \
        python3-pip \
        python3-wheel \
        build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /.venv
ENV PATH="/.venv/bin:$PATH"

COPY ./requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

FROM python:3.13-bookworm as runner

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
      build-essential \
      curl \
      software-properties-common \
      git \
      locales \
      locales-all \
      python3 \
      python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /.venv /.venv

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Usa o ambiente virtual
ENV VIRTUAL_ENV="/.venv"
ENV PATH="/.venv/bin:$PATH"

COPY . .

EXPOSE 8501
ENTRYPOINT [ "streamlit", "run", "1_🏠_home.py", "--server.port=8501", "--server.address=0.0.0.0" ]

