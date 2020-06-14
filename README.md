# Argonauts-Angel Eye_SCDFXIBM
SCDF x IBM Hackathon submission for Team Argonauts

# Table of Contents
* [Proposal](#Proposal)
* [Pitch Video](#Pitch-Video)
* [Architecture of Proposed Solution](#Architecture-of-Proposed-Solution)
* [Detailed Solution](#Detailed-Solution)
* [Getting started](#How-will-you-use-the-software?)
* [What we used](#What-we-used)
* [Acknowledgements](#Acknowledgements)

# Proposal
## Short description

### What's the problem? 
According to a news article published by [The Straits Times](https://www.straitstimes.com/singapore/transport/overall-improvement-in-road-traffic-situation-for-2019-but-more-accidents), it was reported that although fatal accidents and road deaths were at all time low in 2019, there has been an increase in the number of accidents involving eldery pedestrians and motorists. According to statistics (Yusof, 2020), traffic accidents involving eldery pedestrians increased by 33.6 per cent, with the eldery fatality rate increasing by 12.5 per cent in 2019 from 2018. For motorcyclists, the accident rate resulting in injuries rose by 1.9 per cent and motorcyclist and pillion rider fatality rates increased by 3.3 per cent in 2019 from 2018.

<p align="justify">There has also been instances where traffic accidents are unwitnessed or reported only after a period of time which can lead to a delay in emergency resources being activated. SCDF needs to have a better response timing to protect vulnerable road users and ensure that resources are activated efficiently. Currently, the SCDF emergency vehicles are allowed to beat the red light with caution. They have to turn on their blinking lights and sirens and proceed with caution. This will increase the time needed to reach the accident site or hospitals as they do not have a clear wave of green lights.</p>  

### How can technology help?
<p align="justify">Leveraging technology, we can make use of traffic cameras and object detection applications to identify road accidents that require immediate assistance from the SCDF. Some examples include road accidents resulting in fire, overturned vehicles, severe injuries that require medical assistance and road users who are trapped in or under vehicles. Through the use of technology, the machine can be trained to recognise such accidents through footage from traffic cameras to alert the SCDF so they react quickly to the situation. We can also use technology to detect where the emergency vehicle's location to provide clear traffic and the fastest possible route.</p> 

### Our Idea
<p align="justify">As mentioned earlier, it is important that severe road accidents are attended to immediately to lower fatality rates and protect vulnerable road users. Using the data from government websites, we can identify where are the current traffic cameras installed and where severe traffic accidents have occured in the past and pin them on a map. When we overlay the two sets of data, we can identify potential roads that will require traffic cameras to be installed like silver zones or high accident rate areas. Eventually, our goal is to cover all the roads with cameras to ensure that the system can track all road accidents to provide emergency resources in severe cases efficiently.</p> 

<p align="justify">Using IBM's Cloud Annotations Artificial Intelligience and IBM's Watson Machine Learning, we are able to prepare training data and create a machine learning instance. The model will be trained to identify road accidents and classify them according to the different types of accidents. Once the model detects an accident that requires SCDF's assistance, an alert will be sent to SCDF to notify them about the situation. They can then dispatch the nearest SCDF unit to attend to the situation. Together with the data from the traffic cameras and conditions, the system can also map out the fastest possible route to the accident and the fastest route to the nearest hospital if necessary. Using the Green Link Determining (GLIDE) System and traffic cameras, SCDF can link up the traffic lights to provide a clear path of the "green wave" to allow smoother traffic for emergency response vehicles.</p> 

[Back to top](#Argonauts-Solution_SCDFXIBM)

# Pitch Video
![Watch the video](https://i.ibb.co/jW13K8W/Screenshot-2020-06-14-at-5-56-56-PM.png)

Click to watch:
(https://youtu.be/qCy-zFLY3UY)

[Back to top](#Argonauts-Solution_SCDFXIBM)

# Architecture of Proposed Solution

![](https://github.com/ezhentan/Argonauts-Solution_SCDFXIBM/blob/master/Images%20for%20README/IMG_C8A0680A8E89-1.jpeg)

[Back to top](#Argonauts-Solution_SCDFXIBM)

# Detailed Solution
[More details are available here](DESCRIPTION.md)

[Back to top](#Argonauts-Solution_SCDFXIBM)

# How will you use the software?

<strong>First function: Traffic Accident Monitor</strong>
<i>(Model ID: 7a0c9c0c-e820-4aa8-9f80-84d1405a9282)</i><br>
<ol>
  <li>Create the IBM Watson Studio and add in the visual recognition service.</li>
  <li>Launch the Visual Recognition Tool and create an Object Detection Model.</li>
  <li>Upload images into the model.</li>
  <li>Set the labels for each image. For our model we have 5 labels.</li>
    <ul>
      <li>Crashed-Vehicle</li>
      <li>Crashed-Motorcycle</li>
      <li>Fire.Smoke</li>
      <li>Overturned-Light Vehicle</li>
      <li>Overturned-Heavy Vehicle</li>
    </ul>
<i>It is recommended to have at least 50 images for each object as it will allow the machine to detect and discern accidents more accurately.</i><br>
  <li>Train the model.</li>
  <li>Test the model with a new batch of images that is different from the images used for training.</li>
<i>This is to ensure the accuracy of the model even with unseen data.</i>
  <li>Deployment and integration of the model to our solution.</li>
</ol>

<strong>Second function: Traffic Congestion Monitor</strong>
<i>(Model ID: e3a40bc3-3aee-451f-93ab-2d7e31a1e690)</i><br>
<ol>
  <li>Go to IBM Cloud and create the IBM Watson Studio service. </li>
  <li>Create New Project and add Watson – Visual Recognition as an Associated service.  </li>
  <li>Create a Visual Recognition model  </li>
  <li>Upload some images of Traffic congestion in Singapore and train the model. </li>
  <li>In our case, we will be using the traffic images on live traffic conditions from Land Transport Authority (LTA) to analyze congestion live.   </li>
  <i>Refer to "traffic_congestion_monitor.py" for code</i><br>
  <li> Use the live traffic images to test the model </li>
  <li>Deployment and integration of the model to our solution.</li>
</ol>

[Back to top](#Argonauts-Solution_SCDFXIBM)

# What we used
<ol>
  <li>IBM Watson Visual Recognition</li>
    <ul>
      <li>for labelling the type of accidents</li>
      <li>for labelling the traffic flow in the images captured by traffic cameras</li>
     </ul>
  <li>Watson Assistant Machine Learning</li>
  <li>Cloud Object Storage</li>
</ol>

[Back to top](#Argonauts-Solution_SCDFXIBM)

# Acknowledgements
* Yusof, Z. (2020, February 10). Fatal accidents, road deaths at record low in 2019, but more accidents involve elderly and motorcyclists. Retrieved June 14, 2020, from https://www.straitstimes.com/singapore/transport/overall-improvement-in-road-traffic-situation-for-2019-but-more-accidents

[Back to top](#Argonauts-Solution_SCDFXIBM)
