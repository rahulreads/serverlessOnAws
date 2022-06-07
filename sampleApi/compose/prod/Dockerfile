# 
FROM public.ecr.aws/lambda/python:3.8
# 
# 
COPY requirements/prod.txt ${LAMBDA_TASK_ROOT}
# 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r prod.txt

# 
COPY ./src ${LAMBDA_TASK_ROOT}
# 
CMD ["ApiFile.handler"]