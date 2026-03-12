# Molecular Structure Visual Autoencoder 🧪🔬

### Project Description
This project focuses on building and training a Deep Convolutional Autoencoder (CNN) for dimensionality reduction and feature extraction from visual representations of chemical molecules. The model learns to compress 128x128 pixel molecular images into a compact 256-dimensional latent vector and reconstruct them, preserving key topological features like rings, bonds, and heteroatoms.

The dataset is sourced from Kaggle: https://www.kaggle.com/datasets/yanmaksi/big-molecules-smiles-dataset

### Methodology
* **Data Preprocessing:** Generating molecular illustrations from SMILES using *RDKit*.
* **Image normalization** and grayscale conversion for efficient training.
* **Architecture:**
  * Encoder: A deep CNN (4 convolutional layers) that reduces the input (16,384 pixels) to a bottleneck latent vector of 256 (Compression ratio: 64x).
  * Decoder: A symmetrical architecture using Transpose Convolutions to reconstruct the original visual structure.
* **Advanced Training:** Combined Weighted MSE (emphasizing bond structure) and SSIM (Structural Similarity Index) for sharper reconstructions (Hybrid Loss Function).
* **Tools & Frameworks:** *PyTorch*, *RDKit*, *Matplotlib*, *NumPy*.

### Results
* **Performance:** The model achieved a loss of `0.0300`, successfully capturing complex ring systems and small-scale features.
* **Latent Space Validation:** Semantic consistency was verified by calculating Euclidean distances between molecular embeddings; structurally similar compounds cluster together in the latent space.
* **Applications:** Molecular similarity search, virtual screening, and feature extraction for downstream property prediction models.

### Note: 
The training checkpoint and model weights are saved locally. If you need it, please feel free to contact me: <u>marias3753@gmail.com</u>.
