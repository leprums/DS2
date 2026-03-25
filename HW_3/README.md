<img width="1920" height="1920" alt="image" src="https://github.com/user-attachments/assets/59fb0455-b8d7-4b3b-b7be-e193f00c468f" /># AI Gesture Conductor 🎶✨

### Project Description
An interactive, real-time system that bridges computer vision and generative music. By combining human pose estimation with a custom gesture classification model, users can conduct an algorithmic musical piece through physical movement. 

The model (YOLO8) was further trained on data collected manually (./data/collect_data.py) and labeled using Roboflow (https://app.roboflow.com/s-workspace-juute/hands-signs-idwet/1). 
Music was written in Strudel (TidalCycles) - code placed ./data/melody_strudel.js.


[📺 Watch the Video Demo here!](https://drive.google.com/file/d/1P_SLsYVqdpdZagyFjVX_8JSkCtMOk2rq/view?usp=sharing)

### Features
* **Dual-Model Pipeline:** Simultaneously runs *YOLOv8n-pose* for coordinate tracking and a custom-trained YOLOv8 model for gesture recognition (`fist`, `five`, `horns`).
* **Dynamic Audio Control:** Real-time volume and effect modulation based on hand height and clap detection.
* **Immersive Visuals:** Neon trails and screen-wide flash effects synchronized with user interactions.
* **Tools & Frameworks:** *OpenCV*, *YOLOv8n-pose*, *Pygame*, *Strudel*, *Roboflow*.

### Results
* 30 epochs of training, which resulted in **mAP50** - `0.995`, **mAP50-90** - `0.861`.
* **F1-Score** - `0.99` at 0.631 for all three classes.
* **Classes:** fist (Pause), five (Play), horns (Special Effect).
![Results:](https://github.com/leprums/DS2/blob/main/HW_3/data/results/results.png?raw=true) 
![F1 curve:](https://github.com/leprums/DS2/blob/main/HW_3/data/results/BoxF1_curve.png?raw=true)
![Confusion matrix:](https://github.com/leprums/DS2/blob/main/HW_3/data/results/confusion_matrix.png?raw=true)
![Trained model label prediction:](
<p align="center">
  <img src="HW_3/results/val_batch1_pred.jpg" width="600" alt="Trained model prediction">
</p>)

### How to run 
1. Clone the repository:


   `git clone <repository_url>`


   `cd <repository_folder>`


3. Install the dependencies:

   
   Make sure you have a virtual environment activated, then run:

   
   `pip install -r requirements.txt`.


5. Prepare the files:

   
   Ensure that *music.mp3* is located in the same directory as *final_model.py*.


7. Launch the system:

   
   `python final_model.py`.
   
