# Argonauts-Solution_SCDFXIBM
SCDF x IBM Hackathon submission for Team Argonauts

# Table of Contents
* [Proposal](#Proposal)
* [Pitch Video](#Pitch-Video)
* [Architecture of Proposed Solution](#Architecture-of-Proposed-Solution)
* [Detailed Solution](#Detailed-Solution)
* [Getting started](#How-will-you-use-the-software?)
* [What we used](#What-we-used)

# Proposal
## Short description

### What's the problem?
<p align="justify">According to a news article published by The Straits Times in Feburary 2020, it was reported that although fatal accidents and road deaths are at all time low, there has been an increase in the number of accidents involving eldery pedestrians and motorists. According to statistics, traffic accidents involving eldery pedestrians increased by 33.6 per cent, with the eldery fatality rate increasing by 12.5 per cent in 2019 from 2018. For motorcyclists, the accident rate resulting in injuries rose by 1.9 per cent and motorcyclist and pillion rider fatality rates increased by 3.3 per cent in 2019 from 2018. There has also been instances where traffic accidents are unwitnessed or reported only after a period of time which can lead to a delay in emergency resources being activated. SCDF needs to have a better response timing to protect vulnerable road users and ensure that resources are activated efficiently. Currently, the SCDF emergency vehicles are allowed to beat the red light with caution. They have to turn on their blinking lights and sirens and proceed with caution. This will increase the time needed to reach the accident site or hospitals as they do not have a clear wave of green lights.</p>  

### How can technology help?
<p align="justify">Leveraging technology, we can make use of traffic cameras and object detection applications to identify road accidents that require immediate assistance from the SCDF. Some examples include road accidents resulting in fire, overturned vehicles, severe injuries that require medical assistance and road users who are trapped in or under vehicles. Through the use of technology, the machine can be trained to recognise such accidents through footage from traffic cameras to alert the SCDF so they react quickly to the situation. We can also use technology to detect where the emergency vehicle's location to provide clear traffic and the fastest possible route.</p> 

### Our Idea
<p align="justify">As mentioned earlier, it is important that severe road accidents are attended to immediately to lower fatality rates and protect vulnerable road users. Using the data from government websites, we can identify where are the current traffic cameras installed and where severe traffic accidents have occured in the past and pin them on a map. When we overlay the two sets of data, we can identify potential roads that will require traffic cameras to be installed like silver zones or high accident rate areas. Eventually, our goal is to cover all the roads with cameras to ensure that the system can track all road accidents to provide emergency resources in severe cases efficiently.</p> 

<p align="justify">Using IBM's Cloud Annotations Artificial Intelligience and IBM's Watson Machine Learning, we are able to prepare training data and create a machine learning instance. The model will be trained to identify road accidents and classify them according to the different types of accidents. Once the model detects an accident that requires SCDF's assistance, an alert will be sent to SCDF to notify them about the situation. They can then dispatch the nearest SCDF unit to attend to the situation. Together with the data from the traffic cameras and conditions, the system can also map out the fastest possible route to the accident and the fastest route to the nearest hospital if necessary. Using the Green Link Determining (GLIDE) System and traffic cameras, SCDF can link up the traffic lights to provide a clear path of the "green wave" to allow smoother traffic for emergency response vehicles.</p> 

[Back to top](#Table-of-Contents)

# Pitch Video


# Architecture of Proposed Solution


# Detailed Solution


# How will you use the software?


# What we used
1. IBM Cloudant Image Localisation
2. Watson Assistant Machine Learning
3. Cloud Object Storage
