# Submission name
Argonauts: Bird's Eye View_SCDFXIBM

## Section 1
Identifying Accidents Using Object Detection

### Subsection 1.1
To start off, we can identify the traffic camera locations in Singapore and the accident prone areas. Using an overlay on a map, we should be able to see where are the overlaps in areas lacking traffic cameras to monitor the roads. Currently only major expressways have traffic cameras installed to monitor traffic conditions. 

![Traffic Camera Locations in Singapore](https://i.ibb.co/6Y73vbf/Screenshot-2020-06-14-at-12-02-27-PM.png)

For example, Lornie Highway was identified as an accident prone road as it faces heavy traffic during peak hours where there have been many past accidents. However, they do not have a traffic camera installed along that stretch. Other examples may include silver zones where there have been past accidents involving elderly pedestrians. This mapping of traffic cameras can help us better understand which are more vulnerable areas which require more attention from SCDF in the event of a major accident. 

### Subsection 1.2
We will use our custom-trained models to detect serious accidents that require emergency response from SCDF. Using IBM Cloud Object Storage instance, we will store 200 images of different road accidents with different labels to prepare the data for training. There will be **five** main categories of major accidents:
1. Vehicle on fire/smoking
2. Overturned Light Vehicle (Car/Van/Small Truck)
3. Overturned Heavy Vehicle (Large Trucks/Container)
4. Badly Crushed Vehicle
5. Severe Motorcycle Crash

The model will be trained to differentiate between an event (major accident) and non-event (minor accident/no accident) to ensure that SCDF's precious resources are not activated without cause. Using IBM Cloud Annotations, we will localise images within a frame with assigned labels to identify the different types of major accidents that requires SCDF's emergency response. We used a mixture of CCTV footage and images from different angles to train the data in a way such that it is able to recognise the type of accident and discern if emergency response is needed. 

## Section 2
Sending Alerts to SCDF

### Subsection 2.1 


## Section 3 
Deploying Nearest SCDF Unit

## Section 4 
Using Real-time Traffic Conditions to Map Fastest Route



## Conclusion

### Results

## Acknowledgments
