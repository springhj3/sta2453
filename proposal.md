1. Title
Automated Detection of Stellar Flares in TESS Mission Photometric Data
2. Introduction
Briefly introduce stellar flares and their significance in astrophysics.
    Flare is a phenomenon that tremendous amount of energy and light come out momentary. People will be more familiar with solar flare which occurs in the sun's sunspot. However flare can be observed in other stars too especially when their brightness increase and decrease rapidly. 
    Strong flare can impact our life as they can damage spaceship, astronaut, and satellite. It can also make communication disorder. Especially solar flare is one of the important factors when astronaut goes to moon or mars since flare contains a lot of radioactive rays. 
Highlight the challenges in detecting flares (e.g., low-energy flares, quasi-periodic oscillations).
    As stated in README.pdf and Stellar_flares_slides.pdf, there are some challenges such as quasi-periodic oscillations (QPO) in their brightness over time may mimic flares' pattern, and weak flares can be hidden in noises, and some flares happen in very short duration and can be missed in lower cadence data, and without true label, validation algorithm can have low accuracy. 
State the goal: Develop an automated algorithm to detect stellar flares in TESS mission data.
3. Objectives
    Main goal for this project is developing an algorithm that detects stellar flares. I will mainly focus on sudden brightness increase. As mentioned above, QPO in brightness can make false positive so I will figure out how to handle this and will make algorithm to detect low energy flares which can be makred as noises as I mentioned in challenges. 
Create a reliable flare detection pipeline for time-series photometric data.
Address challenges like detrending and low-energy flare detection.
Validate the method across multiple stars (TIC 0131799991, TIC 031381302, TIC 129646813).
4. Data Description
Mention the dataset (PDCSAP Flux data from TESS mission).
Describe its characteristics: brightness time-series with 2-minute cadence.
Note any preprocessing requirements (e.g., cleaning, detrending).
5. Methodology
Data Preprocessing:
Remove trends and noise while preserving flare features.
Flare Detection:
Implement a threshold-based or machine learning model to identify flares (e.g., sudden brightness spikes).
Validation:
Use known flares or synthetic data to evaluate the algorithm.
Metrics: Precision, recall, and F1-score.
6. Reproducibility
Mention tools: Python, lightkurve, Jupyter, GitHub.
Highlight plans for documenting and version-controlling the workflow.
7. Expected Outcomes
A robust algorithm for detecting stellar flares.
Insights into flare frequency and characteristics.
8. Timeline
Week 1–2: Data cleaning and exploratory analysis.
Week 3–4: Develop and test the detection algorithm.
Week 5: Validate on multiple stars and refine the approach.
9. References
Cite relevant papers and guides (e.g., TESS data tutorials, existing detection methods).