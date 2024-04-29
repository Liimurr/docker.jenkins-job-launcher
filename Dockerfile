FROM python:3-slim
ARG JENKINS_URL
ARG JENKINS_USER
ARG JENKINS_PASSWORD

ENV JENKINS_URL=$JENKINS_URL
ENV JENKINS_USER=$JENKINS_USER
ENV JENKINS_PASSWORD=$JENKINS_PASSWORD

ENV TERM xterm-256color
ADD app /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["python", "/app/src/app.py"]