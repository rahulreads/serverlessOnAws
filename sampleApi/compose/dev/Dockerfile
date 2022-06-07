# 
FROM python:3.9
# 
WORKDIR /code
# 
COPY ./requirements/dev.txt /code/dev.txt
# 
RUN python -m ensurepip
RUN pip install -r /code/dev.txt
# 
ADD src /code/src
RUN echo $(ls -1 /code)
# 
CMD ["uvicorn", "src.energyAPI:app", "--host", "0.0.0.0", "--port", "5000"]