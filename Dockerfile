FROM python
COPY . /app
RUN pip3 install flask
RUN pip install --upgrade pip
RUN pip3 install requests
EXPOSE 8081
WORKDIR /app
CMD ["python","app.py"]