# Submission name
Argonauts: Singapore's God Eye_SCDFXIBM

## Section 1
**Identifying Accidents Using Object Detection**

### Subsection 1.1
<p align="justify">To start off, we can identify the traffic camera locations in Singapore and the accident prone areas. Using an overlay on a map, we should be able to see where are the overlaps in areas lacking traffic cameras to monitor the roads. Currently only major expressways have traffic cameras installed to monitor traffic conditions.</p> 

Traffic Camera Locations in Singapore
![Alt Text](https://i.ibb.co/6Y73vbf/Screenshot-2020-06-14-at-12-02-27-PM.png)

Source: https://sgtrafficwatch.org/#

<p align="justify">For example, Lornie Highway was identified as an accident prone road as it faces heavy traffic during peak hours where there have been many past accidents. However, they do not have a traffic camera installed along that stretch. Other examples may include silver zones where there have been past accidents involving elderly pedestrians. This mapping of traffic cameras can help us better understand which are more vulnerable areas which require more attention from SCDF in the event of a major accident.</p> 

### Subsection 1.2
<p align="justify">We will use our custom-trained models to detect serious accidents that require emergency response from SCDF. Using IBM Cloud Object Storage instance, we will store 200 images of different road accidents with different labels to prepare the data for training. There will be five main categories of major accidents:</p>

1. Vehicle on fire/smoking
2. Overturned Light Vehicle (Car/Van/Small Truck)
3. Overturned Heavy Vehicle (Large Trucks/Container)
4. Badly Crushed Vehicle
5. Severe Motorcycle Crash

<p align="justify">The model will be trained to differentiate between an event (major accident) and non-event (minor accident/no accident) to ensure that SCDF's precious resources are not activated without cause. Using IBM Cloud Annotations, we will localise images within a frame with assigned labels to identify the different types of major accidents that requires SCDF's emergency response. We used a mixture of CCTV footage and images from different angles to train the data in a way such that it is able to recognise the type of accident and discern if emergency response is needed.</p> 

## Section 2
**Sending Alerts to SCDF**

<p align="justify">As this is a conceptual idea, we did not do up a code for this part. However, using IBM's Alert Notification system, we can link up the Alert API to receive an alert request from an event that has been triggered (major accident). If the alert matches the rule that has been predetermined, a notification will be sent to the SCDF to follow up with. The SCDF operator who receives the notification can open up the alert to view and deploy the relevant SCDF units if necessary.</p> 

## Section 3 
**Deploying Nearest SCDF Unit**

<p align="justify">Using the traffic camera's location, we can overlay it with a map of the various SCDF stations across Singapore to identify which is the nearest station to the accident. They can then deploy the relevant units from that station to attend to the situation.</p> 

## Section 4 
**Using Real-time Traffic Conditions to Map Fastest Route**

<p align="justify">Using IBM's Visual Recognition tools to develop an application to understand the road conditions in real time. The trained model will be able to tell if the road is crowded and the average time it takes for a vehicle to go past that road. Mapping all the pieces of information together, we are able to create a updated map to identify the fastest possible route for SCDF's emergency vehicles. The system will be updated with live feed from traffic cameras across Singapore. This way, the system will be able to decide which is the best route for the emergency vehicle to take, reducing precious travel time which could result in life or death situations.</p> 


## Conclusion
<p align="justify">In conclusion, our whole solution comprises of integrating "smart infrastructure" to make SCDF's work easier. Through the use of traffic cameras across Singapore, we can have a supervised deep learning framework which allows the system to detect major road accidents which involve vehicular collision (with other vehicles, objects, and pedestrians). This allows for faster reporting and in cases where accidents go unnoticed, SCDF can attend to the situation promptly and save lifes. The traffic cameras also allow for better reporting time and understanding of the situation on SCDF's part. Through larger training data sets and parameters, more can be done to ensure better reliability of the model to increase the model's effectiveness to detect accidents correctly.</p> 

<p align="justify">Traffic cameras and visual recognition systems will also allow SCDF to shave off precious time when responding to emergency situations. Through effective mapping, the emergency vehicle will be able to reach the accident site and the hospital in shorter periods of time by prediciting the fastest route and ensuring that the emergency vehicles are able to catch the "green wave" of traffic lights by linking the GLIDE system to emergency vehicles.</p> 

### Results

## Acknowledgments
