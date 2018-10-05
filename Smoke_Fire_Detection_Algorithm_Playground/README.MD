	- Finish current filter code to ZOOM IN on the area with smoke, select that, and send to the CNN
	- CNN uses color vals and stuff from the smoke images to then CONFIRM that the image actually contains SMOKE and FIRE!
	- If it does not detect fire, check the 'gradient' or slope of the smoke, go down in the original a certain amount according to the slope, then redetect to find the origin
	- END GOAL : Find the origin of the fire in the current frame and bounding box it, also bounding box the smoke
	- Explain logic behind why we look for the smoke first, then look for the fire (smoke bigger, etc…)
	- Also implement detection of motion
    
    
    
# File States

* Fire detection python notebook works.
* Smoke detection python notebook does not.
* Folder fill with old non functional code, saved for versioning and just in case
* Model Creation folder
    - Contains A TON of models I made for fun to test