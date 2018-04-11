
# Jdoctr.py
# Simple utility to format JSON for use in a javadoc.
#
# Example:
#
# Input:
# {"greeting": "Hello!"}
#
# Output:
# * <pre>
# * {
# *     "greeting": "Hello!"
# *  }
# * </pre>
#
# By Andrew Garner 2018

import json
import sys
import argparse

# Shows help
parser = argparse.ArgumentParser(description='Utility for making JSON paste-able into a Javadoc. Adds asterisks and <pre> tags.')
args = parser.parse_args()

# Get Input from user
inputJson = input('Enter JSON: ')

# Parse JSON
try:
	parsedJson = json.loads(inputJson)
except ValueError as error:
	print("Bad JSON input: ", str(error))
	quit()
except:
    print("Unexpected error: ", sys.exc_info()[0])
    raise

# format input
formattedJson = json.dumps(parsedJson, indent=4, sort_keys=False)
# Add asterisks to all lines, preserving new lines
formattedJson = formattedJson.replace('\n', '\n* ')
# Add pre tags
formattedJson = "\n* <pre>\n* " + formattedJson + "\n* </pre>\n"
# Return
print(formattedJson)