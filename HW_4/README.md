# DS-Assistant Bot 🤖

### Project Description
This project implements a task-oriented chatbot that classifies user intentions (intents) using a neural network. It helps beginners with Git commands, virtual environments, and VS Code shortcuts. 

tg-bot: [@my_DS_assistant_bot](https://t.me/my_DS_assistant_bot)

### Features
* **Custom Architecture:** Hidden layer size (16), automatically adapting to the input vocabulary (Bag of Words).
* **Modular Design:**  Separation between model architecture (`model.py`), training logic (`train.py`), the terminal bot interface (`terminal_test.py`) and the Telegram bot interface (`bot.py`).
* **Dynamic Checkpoints:** Model metadata (vocabulary, tags, hidden size) is stored within the `.pth` file, allowing the bot to sync with new training versions automatically.
* **Tools & Frameworks:** *PyTorch*, *NLTK (SnowballStemmer)*, *Aiogram (2.25.1)*.

### How to run 
1. Clone the repository:

   `git clone <repository_url>`

   `cd <repository_folder>`

3. Install the dependencies:
   
   Make sure you have a virtual environment activated, then run:
   
   `pip install -r requirements.txt`.

4. Train the Model:

   Run the training script to generate the `model.pth` file:

   `python train.py`

5.1. Launch the Bot in the terminal:

   `python terminal_test.py`

   OR
   
5.2. Configure your Telegram Token:
   
   Get your token from @BotFather. Open the .env.example file in the root directory and change code:
   
   `BOT_TOKEN=your_api_token_here`
   
   Change the extension of this file to .env .

### Data Structure
The bot's knowledge is stored in `config.json`. You can easily add new intents by following the existing JSON format. 
Note that you need to run `train.py` again after changing `config.json` and before running the bot in the terminal or as tg-bot.
