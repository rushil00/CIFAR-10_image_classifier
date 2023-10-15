# Use an official PyTorch image as the base image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# To add and Install any additional dependencies required for code in future
RUN pip install jupyter

# Expose port for Jupyter Notebook (default is 8888)
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]