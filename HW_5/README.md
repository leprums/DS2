# Emoji Generative Adversarial Network (GAN) 🤗👩‍💻🏳️

### Project Description
This project implements a deep convolutional generative adversarial network (DCGAN) for generating unique emoji. The model is trained on a dataset containing thousands of different icons and learns to create new images, progressing from random noise to meaningful visual images.

The dataset is sourced from HuggingFace: https://huggingface.co/datasets/BioMike/emoji-vae-dataset

### Features
* **DCGAN Architecture:** Uses convolutional layers (`Conv2d`) in the Discriminator and transposed convolutions (`ConvTranspose2d`) in the Generator.
* **Advanced Training:** Uses Instance Noise to prevent the Discriminator from dominating.
* **Dynamic Checkpoints:** Preserving weights (`.pth`) for incremental model improvement. Retraining after 100 epochs with a lover learning rate.
![Loss:](https://github.com/leprums/DS2/blob/main/HW_5/results/output_150.png?raw=true)
* **Tools & Frameworks:** *PyTorch*, *Torchvision*, *Matplotlib*, *Imageio* (for creating GIF progress animation).

### Results
The model shows the evolution from chaotic pixels at epoch 0 to the formation of color zones, geometric shapes, and recognizable emoji faces by epoch 150.
![Results:](https://github.com/leprums/DS2/blob/main/HW_5/results/gan_emoji_evolution.gif?raw=true) 

### Note: 
The training checkpoint and model weights are saved locally. If you need it, please feel free to contact me: <u>marias3753@gmail.com</u>.
