import argparse
import json

def processCommandLineArgs(file):
    cmdLineArgsDict = json.load(open(file))
    parserObj = argparse.ArgumentParser(description="Process Command line arguments")
    for option in cmdLineArgsDict:
        cmdLineArgsArr = [f"'{option}'"]
        for optVal in cmdLineArgsDict[option]:
            if (type(cmdLineArgsDict[option][optVal]) == str):
                cmdLineArgsArr.append(f"{optVal}='{cmdLineArgsDict[option][optVal]}'")
            else:
                cmdLineArgsArr.append(f"{optVal}={cmdLineArgsDict[option][optVal]}")
        cmdLineArgsStr = ",".join(cmdLineArr)
        cmdLineArgsStr = f"parserObj.add_argument({cmdLineStr})"
        ret = eval(f"{cmdLineArgsStr}")
    cmdLineArgs = parserObj.parse_args()
    return cmdLineArgs
