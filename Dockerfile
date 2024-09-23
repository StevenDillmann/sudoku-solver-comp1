# Use a base image that includes Conda
FROM continuumio/miniconda3

# Set the working directory in the container
RUN mkdir -p sd2022

# Copy your application code into the container
COPY . /sd2022
WORKDIR /sd2022

# Install python3-dev for memory_profiler
RUN apt-get update && \
    apt-get install -y gcc python3-dev

# Create the environment: sd2022_c1_env
RUN conda env update --file environment.yml --name sd2022_c1_env && \
    echo "conda activate sd2022_c1_env" >> ~/.bashrc

# Make sure the conda environment is activated
SHELL ["/bin/bash", "--login", "-c"]

# Install 'glpk-utils' module for lp solver
RUN apt-get update && apt-get install -y glpk-utils
