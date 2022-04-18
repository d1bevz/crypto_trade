FROM airflow-lite

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  emacs \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf "/var/lib/apt/lists/*" \
  && apt install wget -y

USER airflow
COPY ./requirements.txt .
RUN pip install -r requirements.txt