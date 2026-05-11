# Reagents Search Bot 🧪

### Project Description
A neural network-based Telegram bot for searching chemical reagents within a laboratory (the primary language is Russian; chemical formulas searches are conducted in English).

### Features
* **Semantic Search Engine:** Implements a vector-based search using the `multilingual-e5-small` transformer model, allowing the bot to understand the context and synonyms of chemical reagents beyond simple keyword matching. (https://huggingface.co/intfloat/multilingual-e5-small)
* **Chemistry-Aware Logic:** Includes a custom scoring algorithm that provides "exact match" bonuses for chemical formulas and names, ensuring high precision when searching for specific reagents.  
* **Automated Data Pipeline:** Features a self-contained preprocessing script (`data_processor`) that handles Excel parsing, text passage formation, and vector embedding generation automatically upon startup.
* **Docker-Ready Architecture:** Fully containerized environment with optimized *.dockerignore* and *docker-compose* configurations, enabling one-click deployment while keeping heavy model weights and environment files outside the container image.
* **Tools & Frameworks:** *PyTorch*, *Sentence-Transformers* (Hugging Face), *Aiogram (3.27.0)*, *Docker*.

## How to run 

### Option 1: Local Deployment (Manual)

1. Clone the repository:

   `git clone <repository_url>`

   `cd <repository_folder>`

2. Set up a Virtual Environment: 

   To avoid version conflicts, it is recommended to use a virtual environment:

   `python -m venv venv`

   *Activate on Windows:*

   `.\venv\Scripts\activate`

   *Activate on Linux/Mac:*

   `source venv/bin/activate`

3. Prepare the Data: 

   The file `data/raw/reagents_raw.xlsx` is a demo version of the reagent database. You can edit this file while maintaining its original table structure.

4. Install the dependencies:
   
   Make sure you have a virtual environment activated, then run:

   `pip install -r requirements.txt`.

5. Process Data: 

   Run the data processor to download the model and generate embeddings:

   `python -m src.data_processor`

   *Note: On the first run, the system will automatically download the neural network to the `models/` folder and save the vector representations.*

6. Configure Bot Responses: 

   If necessary, edit the bot's response scenarios in `intentions.json`.

7. Terminal Test: To verify the search logic without Telegram, run:
   
   `python -m src.terminal_test`

8. Configure Telegram Bot:

   Get your token from @BotFather. Open the *.env.example* file in the root directory and change code:
   
   `BOT_TOKEN=your_api_token_here`
   
   Change the extension of this file to *.env* .

9. Run the Bot:

   `python -m src.bot`

### Option 2: Docker Deployment

1. Clone the repository:

   `git clone <repository_url>`

   `cd <repository_folder>`

2. System Requirements: 

   Ensure that *Docker* and *Docker Desktop* are installed and running.

3. Configure Telegram Bot:

   Get your token from @BotFather. Open the .env.example file in the root directory and change code:
   
   `BOT_TOKEN=your_api_token_here`
   
   Change the extension of this file to *.env* .

4. Build and Launch: 
   Run the following terminal command to build the image and start the container in the background:

   `docker-compose up -d --build`

*Note: On the first start, the system will automatically download the neural network into the models/ folder and process the data. The bot will be available in Telegram immediately after the process finishes.*

### Data Structure
* **Intent Management:** The bot's conversational logic is stored in `intentions.json`. You can expand the bot's capabilities by adding new intents following the existing JSON schema.
* **Knowledge Base:** Reagent data is managed via `data/raw/reagents_raw.xlsx`. You can customize the searchable database by modifying this file, provided the original table structure and column headers remain intact.