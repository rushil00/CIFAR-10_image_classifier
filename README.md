# CIFAR-10 Classifier
This repository consists of my work on the CIFAR-10 Dataset with Pytorch Framework for Image Classification using various interesting Deep Learning Architectures (Starting with LeNet and ResNet).
- I have previously worked with TensorFlow in my introductory coursework, but this was a thrilling experience because it challenged my intellect and really captured my interest in the Pytorch framework, hence I am motivated to explore this further.
- This has also been a nice opportunity for me to revise the Deep Learning and ML concepts that I am familiar with. Moreover, I also came across some interesting papers while making this project which I will definitely find time to read.
<li>LeNet.py is a LeNet model designed using pytorch from SCRATCH and used throughout the project. The pytorch-provided ResNet-18 Model is also used for comparison of metrics.
<li>This project aims to develop my foundational understanding of Deep Learning in Computer Vision.</li>
<li>This Project is Deployed on EC2 instance with the live link of Jupyter Notebooks given in the below section.
<h2>How to Navigate this project?</h2><br>There are two ways in which you can make use of this project: <br>
<ol>
    <h4>STRUCTURE</h4>

        ./cifar.ipynb ==> Main code notebook, where all the models are implemented and their performances are compared.
        ./pruning.ipynb ==> A notebook to get a better understanding of regularization of deep learning model
        ./models/ ==> A directory where all the models (pruned and not-pruned are saved as .pth files)
        ./test.ipynb ==> Jupyter Notebook for TESTING on random test images by classifying them and then comparing with the true label.
<br>
<li>Run and Edit it as you want on the following link: <a href=http://34.229.19.142:8888/tree?token=42c7508caeba1b539955bd1a5ff14e785418f6a12d9b0773>CLICK HERE</a> <br> <t>This is a hosted & Deployed Docker image on AWS EC2 instance</t></li> <br> 

<li>Run it locally, meaning we have to clone this git repo and then run the Dockerfile present in the working directory, as follows:  
    <ul><li>

    git clone https://github.com/rushil00/CIFAR-10_image_classifier/
    cd path/to/cloned/repo/CIFAR-10_image_classifier
    docker run -d -p 8888:8888 cifar-10_classifier:latest
 </li><br>
 <li>For Installation and Setup of Docker, refer to its documentation: <a href=docs.docker.com>Here</a></li></ul>
 </li>
</ol>
<h2>Following deliverables are provided through this project:-</h3>
<ul>
    <li>Python Model training (with and without Pruning) in a Jupyter Notebook, while also providing the model ".pth" files for future uses.</li> 
    <li><b>Trained Model Files</b> in the "./models/" folder ["modelLeNet.pth" , "modelResNet.pth"].</li>
    <li><b>Pruned Model Files</b> in the "./models" folder ["prunedLeNetModel.pth" , "prunedResNetModel.pth"].
    <li> A report ("./SummaryReport.pdf") summarizing the results, including the accuracy achieved by the original model, the pruning ratio chosen, the accuracy achieved by the pruned model, and the reduction in model size.
</ul>
<h2> Deployment Process and Testing (EC2, etc.)</h2>
<ul>
    <li>The Docker image was first publicly built and uploaded via local, to docker-hub as well as ECR (Elastic Container Registry) - An AWS Platform to manage Containerization</li>
    <li>Then, an EC2 instance was launched, and I set the security groups to allow traffic on 8888 port of the instance because that is usually associated with Jupyter Notebooks</li>
    <li>After EC2 instance was set, the Docker Image was pulled from the ECR with the following command (after I made sure that I have logged in with the aws CLI):
        
        docker pull public.ecr.aws/s3q3e2f3/cifar-10-classifier:latest
</li>
    <li>Post the docker setup and deployment on EC2 instance, I ran with the [`docker run`] command stated before </li>
    <li>For unit testing, I wrote the code and implemented unittesting.py</li>
    <li><h3>Further GOAL:</h3> Given some more time, I would like to use my ELK Stack Skills and configure the Analytics and Results for this model too. I am a keen learner and problem solver, given an opportunity, I would not disappoint</li>
</ul>
<h2>Link to the Report based on this project:-</h2>
<ol><li type=none><h3><a href="https://docs.google.com/document/d/1JVEw5I6S3AD6iyPr9fjowG7rSYUgez2ruutxTCtZcGY/edit?usp=sharing">Click Here</a>
<br></h3> This is a Google Document. Feel Free to comment.
<br> 



