import os
import time
import argparse
import subprocess

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

with open('output.txt','w') as outfile:
    for file in sorted(os.listdir(location)):
            if file != "order_details.txt" and file != "done" and file != "output.txt":
                    result = 1
                    i += 1
                    while result != 0:
                            cmd = "node . mint " + args.address + " '" + location + file + "' " + args.fee
                            print(cmd)
                            result = subprocess.check_output(cmd)
                            #outfile.write(output + "\n")
                            #result = os.system("node . mint " + args.address + " '" + location + file + "' " + args.fee)
                          
                            print("Output: " + str(result))
                            time.sleep(1.0)
                            if "txid" in result:
                                    os.system("mv" + " '" + location + file + "' " + location + "done/")
                                    print("Count: " + str(i))
