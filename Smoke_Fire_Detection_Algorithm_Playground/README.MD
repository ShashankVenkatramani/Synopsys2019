	- Finish current filter code to ZOOM IN on the area with smoke, select that, and send to the CNN
	- CNN uses color vals and stuff from the smoke images to then CONFIRM that the image actually contains SMOKE and FIRE!
	- If it does not detect fire, check the 'gradient' or slope of the smoke, go down in the original a certain amount according to the slope, then redetect to find the origin
	- END GOAL : Find the origin of the fire in the current frame and bounding box it, also bounding box the smoke
	- Explain logic behind why we look for the smoke first, then look for the fire (smoke bigger, etc…)
	- Also implement detection of motion
    
    
    
# File States

* A LOT OF THE CODE WAS MOVED AROUND, MANY DATA DIRECTORIES NO LONGER FUNCTION IN THE CODE
* CODE IS ORGANIZED BY DATE AND FUNCTIONALITY AS OF OCT 5 - 2018