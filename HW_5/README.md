# Emoji Generative Adversarial Network (GAN) 🤗👩‍💻🏳️

### Project Description
This project implements a Deep Convolutional Generative Adversarial Network (DCGAN) for generating unique emojis. The model is trained on a dataset containing thousands of different icons and learns to create new images, progressing from random noise to meaningful visual patterns.

The dataset is sourced from HuggingFace: https://huggingface.co/datasets/BioMike/emoji-vae-dataset

### Features
* **DCGAN Architecture:** Uses convolutional layers (`Conv2d`) in the Discriminator and transposed convolutions (`ConvTranspose2d`) in the Generator.
* **Advanced Training:** Uses Instance Noise to maintain training stability and prevent Discriminator dominance.
* **Dynamic Checkpoints:** Supports incremental model improvement by saving/loading weights (`.pth`). Includes a refining stage (training beyond 100 epochs with a lower learning rate for better detail).
![Loss:](https://github.com/leprums/DS2/blob/main/HW_5/results/output_150.png?raw=true)
* **Tools & Frameworks:** *PyTorch*, *Torchvision*, *Matplotlib*, *Imageio* (for creating GIF progress animation).

### Results
The model demonstrates an evolution from chaotic pixels at epoch 0 to the formation of distinct color zones, geometric shapes, and recognizable emoji faces by epoch 150.
![Results:](https://github.com/leprums/DS2/blob/main/HW_5/results/gan_emoji_evolution.gif?raw=true) 

### Note: 
The training checkpoint and model weights are saved locally. For access or inquiries, please feel free to contact me: <u>marias3753@gmail.com</u>.
