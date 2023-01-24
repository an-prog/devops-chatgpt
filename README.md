---
id: g2ye3bmmt1em54kdhmhbni0
title: README
desc: ''
updated: 1674586214764
created: 1674586214764
---
# notes
This is sample code to illustrate how to use chatgpt API and dockerize it in container and deploy it on kubernestes cluster 

Pre-requisite
Step 1. Install Docker Desktop
Download and install Docker Desktop using this link.

Step 2. Enable Kubernetes
Open Docker Dashboard > Settings > Kubernetes > Enable Kubernetes.

Step 3. Update the key in python script and update the query you want to run

In this script, the openai library is imported, and it’s used to interact with the GPT-3 API.

Next, An API_KEY is added. This is a required step to access the GPT-3 API.
Then, a function generate_text() is defined which takes a prompt as input and returns a generated text as output. Inside the function, openai.Completion.create() is called to generate text based on the prompt. The engine, prompt, max_tokens, n, stop and temperature arguments can be adjusted to suit your specific needs.

Finally, the script calls the generate_text() function with a specific prompt and assigns the output to the generated_text variable, which is then printed to the console.

Step 4. API key - Where to fetch it and run docker
Once you create an account with OpenAI, you will need to add your OpenAI Keys by adding it to this line of the script:

openai.api_key = "YOUR_API_KEY"
Once you have made the changes, it’s time to build the image by running the following command:
docker build -t dockerrepo/dockername .

Step 5. Run docker and see the magic !! You can docker logs to validate.

Step 6. chatgpt-deployment in kubernetes cluster
Create a kubernetes cluster and use chatgpt-deployment.yaml
that creates a single replica of the Chat GPT container. The container image is specified in the “image” field, and the ports exposed by the container are defined in the “ports” field. The resources field defines the memory and CPU limits and requests for the container.

Step 7. Create service in kubernetes cluster to let world access your magic 
Use chatgpt-service.yaml by running kubectl apply -f filename

This YAML file creates a Service named “chatgpt-service” that routes traffic to the Chat GPT pods, and it should be used in combination with the Deployment YAML file to deploy the service.
Please keep in mind this is just a basic example, and you may need to modify it to suit your specific use case.

Conclusion
It was fun containerising Chat GPT and running it as a Docker container. All the above steps have been tested on Docker Desktop enabling Kubernetes. With Chat GPT, there is a great opportunity to build, share and deploy Docker containers on multiple platforms and deploying it on Kubernetes Cluster