FROM jupyter/minimal-notebook

# RUN pip install jupyterthemes
# RUN pip install --upgrade jupyterthemes
RUN pip install intersystems-irispython

COPY kernel.py /objectscriptkernel/
COPY kernel.json /objectscriptkernel/

RUN jupyter kernelspec install --prefix=$CONDA_DIR /objectscriptkernel/

# RUN jt -r
USER root

COPY start-notebook.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/start-notebook.sh
