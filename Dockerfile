FROM yoanlin/opencv-python3

RUN mkdir /app
WORKDIR /app
RUN cd /app
RUN git clone https://github.com/shantnu/FaceDetect.git

COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]