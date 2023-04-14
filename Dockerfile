FROM python:3.10
WORKDIR /RESTChessSolver
COPY requirements.txt /RESTChessSolver/
RUN pip install -r requirements.txt
COPY . /RESTChessSolver
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]