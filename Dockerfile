FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /portfolio_project
COPY requirements.txt /portfolio_project/
RUN pip install -r requirements.txt


CMD ["echo", "Docker image built"]

