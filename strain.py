import os, time

# get threshold or use default of 0.3
thresh = input("Recognition threshold (Reccomend 0.3): 0.") or "3"
# set up the terminal command
weights = "../yolo9000-weights/yolo9000.weights"
pre = "./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg" + " " + weights
post = "-thresh 0." + thresh
os.mkdir("../classifiedFrames")

# for every frame
for file in os.listdir("../frames"):
	# as to ignore system or empty files
    if "out" in file:
		# run the concatenated command with the input frame
        os.system(pre + " ../frames/" + file + " " + post)
		# wait for the command to finish and the prediction file to be made
        while os.path.isfile("predictions.png") == False:
            time.sleep(0.2)
		# once the file is made, wait for data to finish copying
        time.sleep(0.5)
		# move the file into a finished frame folder
        os.rename("predictions.png", "../classifiedFrames/" + file)