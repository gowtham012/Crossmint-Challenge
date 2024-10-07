
# Crossmint - Create your own megaverse challenge  

### Hi, I'm Gowtham Kumar Solleti ! 👋 
#### I'm a software engineer with a passion for developing robust and scalable solutions, and my current interest lies in exploring the exciting world of Web3. 

This project, Megaverse Builder, was created as part of a coding challenge that involved interacting with the Crossmint Megaverse API. The goal of this project is to construct a 2D space known as the Megaverse, filled with different celestial objects such as Polyanets, Soloons, and Comeths, based on a predefined map.


## Introduction

### Project Overview:

The Megaverse Builder project is part of a crossmint coding challenge that involves creating and managing a 2D space called the Megaverse. 

The Megaverse consists of various celestial objects such as:

🪐 Polyanets

🌙 Soloons (in various colors)

☄️ Comeths (moving in various directions)

The whole project is to interact with the Crossmint Megaverse API to generate these objects based on a goal map(predefined).

### Code structure:
This code is divided into two classes:

#### 1. MegaverseAPI

MegaverseAPI mainly handles all interactions with the Crossmint API. It fetches the goal map and posts celestial objects such as Polyanets, Soloons, and Comeths. I also implemented Logging, Error Handling, and Retry Mechanisms, which indicates little over-engineering for this project. Usually, I use AWS CloudWatch for logging and monitoring, but for this project, I used a logging module in Python.

#### 2. Build_Megaverse

Build_Megaverse processes the goal map and creates the required celestial objects based on the object type (Polyanets, Soloons, or Comeths) and their positions in the map. It calls the MegaverseAPI to create the correct objects at the right positions.

#### Usage

##### 1. Clone the repository:
```
git clone https://github.com/gowtham012/Crossmint-Challenge.git
cd Crossmint-Challenge
```

##### 2. Install dependencies:
```

pip install requests
pip install urllib3
```
##### 3. Run the script:
```
 python Crossmint-main.py
```


#### Note

I tried implementing both multithreading with dedicated workers, but I didn't achieve an optimal solution and encountered some warnings about the workers. The code is now error-free, and the time taken is the same as when I used multithreading.

### Images
#### With Multithreading
<img width="1017" alt="Screenshot 2024-10-07 at 10 45 35 am" src="https://github.com/user-attachments/assets/ae435630-f236-49d8-86bf-6f9364a012b2">

#### Without Multithreading
<img width="1017" alt="Screenshot 2024-10-07 at 10 46 00 am" src="https://github.com/user-attachments/assets/8ed81300-e900-46e4-a4fa-1830ccb405e9">

#### Final Map
<img width="1017" alt="Screenshot 2024-10-07 at 10 57 41 am" src="https://github.com/user-attachments/assets/ac35c56e-a2eb-4731-957b-da82d0972c6c">



### Contact
Please let me know if you have any questions regarding the task.
Email: gsollet1@binghamton.edu
