FROM jupyter/base-notebook:db3ee82ad08a
MAINTAINER PlantCV <ddpsc.plantcv@gmail.com>

USER $NB_USER

# Install Binder requirements
RUN pip install --no-cache-dir vdom==0.5

# Install OpenCV with conda
RUN conda install --quiet --yes --channel conda-forge opencv=3.3.0 git

# Clone PlantCV
WORKDIR $HOME
RUN git clone https://github.com/danforthcenter/plantcv.git
WORKDIR $HOME/plantcv

RUN echo $PYTHONPATH

# Install PlantCV Python prerequisites and PlantCV
RUN pip install --no-cache-dir --quiet -r requirements.txt && python setup.py install
