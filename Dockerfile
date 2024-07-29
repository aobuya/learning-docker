FROM python
COPY . /app
WORKDIR /app
CMD ["app.py","python"]