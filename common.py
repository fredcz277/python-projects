import argparse
import json

def processCmdLineArgs(file):
    cmdLineDict = json.load(open(file))
    parserObj = argparse.ArgumentParser(description="Process Command line arguments")
    for option in cmdLineDict:
        cmdLineArr = [f"'{option}'"]
        for optVal in cmdLineDict[option]:
            if (type(cmdLineDict[option][optVal]) == str):
                cmdLineArr.append(f"{optVal}='{cmdLineDict[option][optVal]}'")
            else:
                cmdLineArr.append(f"{optVal}={cmdLineDict[option][optVal]}")
        cmdLineStr = ",".join(cmdLineArr)

        cmdLineStr = f"parserObj.add_argument({cmdLineStr})"
        ret = eval(f"{cmdLineStr}")
    cmdLineArgs = parserObj.parse_args()
    return cmdLineArgs
