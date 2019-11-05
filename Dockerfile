FROM python:3.7

RUN mkdir /e_l_p
# Set work-directory to e_l_p
WORKDIR /e_l_p

# # Copy the current directory contents into the container at /e_l_p
COPY . /e_l_p


RUN pip install pipenv

RUN pipenv install

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
