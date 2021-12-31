FROM python:3.6

WORKDIR /usr/src/app

RUN wget -O repo.zip https://github.com/slix/scrapy/archive/2b30e0b89d0de2b735ae4040d309de8fa606bded.zip && unzip repo.zip && rm repo.zip && mv scrapy-2b30e0b89d0de2b735ae4040d309de8fa606bded/ scrapy-repo/

RUN pip install --no-cache-dir setuptools==59.6.0 pip==21.3.1 wheel==0.37.1
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e scrapy-repo/

WORKDIR scrapy-repo/

ENV MONKEYTYPE_TRACE_MODULES=scrapy,parsel,w3lib,itemadapter,itemloaders,cssselect,queuelib
RUN monkeytype run -m pytest -- --durations=10 docs scrapy tests --reactor=default \
    && monkeytype run -m pytest -- --durations=10 docs scrapy tests --reactor=asyncio \
    && xz -v -9 monkeytype.sqlite3

COPY ./run-on-all-files.py ./run-on-all-files.py
RUN python run-on-all-files.py
RUN unxz monkeytype.sqlite3.xz --keep && python run-on-all-files.py && rm monkeytype.sqlite3
