# Generative-Adversarial-Bots

## What are Generative Adversarial Bots?
Briefly, Generative Adversarial Bots (GABs) are bots that are pitched up against each other, and generate a conversation that is used to train a third bot.

## Motivation
With the increasingly competitive environment of chatbots, many companies have to spend more money, time and energy on improving their technologies and research projects to match the level of competitors. To test them, developers need a massive amount of users to chat with their bots, so they can collect data and analyze it to decide on how to optimize their chatbot.

We wish to change that by proposing a novel approach to testing, evaluating and optimizing chatbots. The first part of the approach involves the application of currently available technologies, and massively utilize them. The second part involves the implementation of recent research papers into our Python code.

## Inspiration
One of the main paper that inspired our choice of project was Ian Goodfellow's paper on ["Generative Adversarial Models"](https://arxiv.org/abs/1406.2661), also known as GANs. His work inspired many publications in Computer Vision and NLP, and inspired us by their use of generative and discriminative models.

Instead of using Neural Networks as models, we pair up chatbots and generate conversations until we deem it sufficient. We then evaluate the quality of the conversations using the Turing Test (with humans). The best conversations are then selected according to their score, and are fed to our third (external) bot.

## Choice of Conversation Type
We decided to use bots specialized in "Small Talks", since they are more easily available, and it is easier to generate and keep the conversations going. With the time constraint, we did not have the chance to port the approach to functional and intent-based bots. However, it is definitely something we are interested in doing, especially with the exciting **FigureQA** datasets recently released by **Maluuba**, as well as the solid API provided by **Nuance**.

## Adversarial Conversations
The adversarial nature of project lies in the attempt of the bot to stay coherent in a general conversation. If the bot starts showing signs of incoherence, or display bot-like behaviour, they will be heavily punished during the Turing Test. Therefore, such behaviour will not be transmitted to our external bot.

## Challenges and Solutions
The implementation of bots took much longer than expected. There were almost no web APIs of pretrained models, instead in most cases they had to be trained by us. For this reason, we chose to use the ChatterBot library in Python, which permitted us to start testing and create working models quickly. We also used the CleverBot's web API, which was simple to use, yet very powerful due to its immense database stemmed from millions of users dialogues.

## Data to Train Models
Although the Cleverbot API did not require any training, we had to train our ChatterBot. We decided, for this hack, to use some of the readily available datasets: the default corpus, the Cornell Movie Dialog Corpus, and the Ubuntu Dialogue Corpus.

To accelerate the process, and ensure that it is done quickly but smoothly, we used the **Microsoft Azure** Virtual Machines to train our models simultaneously. Although it's our first use of the VMs, we are excited to see what Azure can do when we will scale up the model trainings.

## The Interactions Illustrated
[https://github.com/xhlulu/Generative-Adversarial-Bots/blob/master/interactions_illustrated.jpg]

## Next Steps
Before all, our project is a rough prototype of what we have in mind. In term of chatbots, we are planning to add Amazon Lexa and Google Assistant, as well as use the platforms by Nuance MIX, API.ai and Microsoft Cognitive Toolkit. To train those chatbots, we are planning to find more dialogue corpus to create exotic chatbots. 

Ultimately, we wish to reduce the human-factor as much as possible by implementing Turing Test-inspired computing methods, as described in [this paper](https://arxiv.org/pdf/1701.06547.pdf). Other than this test, we are interested in exploring different types of metrics, which are describe in [this systematic review](https://arxiv.org/ftp/arxiv/papers/1704/1704.04579.pdf). If done well, our prototype has a lot of potential to save a lot of time and energy in term of generating samples for chatbots, as well as providing an alternative method to create a strong chatbot from scratch.

## Links
Here's our Google Slides: [link](https://docs.google.com/presentation/d/1MjSdeB57STukNT04J7WG1fOLMiktLi9YsH4rbOxnznI/edit?usp=sharing)
