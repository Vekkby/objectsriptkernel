FROM jupyter/minimal-notebook

USER $NB_UID
RUN fix-permissions /etc/jupyter/
COPY start-notebook.sh /usr/local/bin/

COPY irisnative-1.0.0-cp34-abi3-linux_x86_64.whl /tmp/
RUN pip install /tmp/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl

COPY kernel.py /objectscriptkernel/
COPY kernel.json /objectscriptkernel/

RUN jupyter kernelspec install --prefix=$CONDA_DIR /objectscriptkernel/

USER root
RUN rm -rf /tmp/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl