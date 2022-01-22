FROM openjdk:11
EXPOSE 8080
ADD app.py app/
CMD python app.py