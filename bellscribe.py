import os
import time
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--address', type=str, required=True)
parser.add_argument('--order', type=str, required=True)
parser.add_argument('--fee', type=str, required=True)
# Parse the argument
args = parser.parse_args()

location = "/mnt/blockstorage/order-files/" + args.order + "/"

i = 0

os.system("mkdir " + location + "done")

with open('output.txt','a') as outfile:
    for file in sorted(os.listdir(location)):
            if file != "order_details.txt" and file != "done" and file != "output.csv":
                    result = 1
                    i += 1
                    while result != 0:
                            cmd = "node . mint " + args.address + " '" + location + file + "' " + args.fee
                            print(cmd)
                            outfile.write(os.popen(cmd).read()+"\n")
                            #result = os.system("node . mint " + args.address + " '" + location + file + "' " + args.fee)
                          
                            #print("Output: " + str(result))
                            time.sleep(0.5)
                            if result == 0:
                                    os.system("mv" + " '" + location + file + "' " + location + "done/")
                                    print("Count: " + str(i))
                            if result == 512:
                                    #skip to next file
                                    result = 0  
