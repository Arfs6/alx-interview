#!/usr/bin/python3
"""Parsing logs
Input from stdin.
Computes matrix after 10 lines or
after KeyboardInterupt
"""

import sys
import re


def showMatrix(totalFileSize, statusCodeCount):
    """Display current matrix."""
    print("File size:", totalFileSize)
    for statusCode, count in statusCodeCount.items():
        if count:
            print(statusCode + ":", count)


def run():
    """Begin code execution."""
    lastStopped = 0
    totalFileSize = 0
    statusCodeCount = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    regex = (
        r"\d+\.\d+\.\d+\.\d+ "
        r"- \[[^\]]+\] "
        r'"GET /projects/260 HTTP/1\.1" '
        r"(.+) (\d+)"
    )
    pattern = re.compile(regex)

    while True:
        try:
            log = input()
        except KeyboardInterrupt as mess:
            showMatrix(totalFileSize, statusCodeCount)
            raise mess
        except EOFError:
            break
        lastStopped += 1
        match = pattern.match(log)
        if match is None:
            continue
        statusCode = match.group(1)
        if statusCode in statusCodeCount:
            statusCodeCount[statusCode] += 1
        totalFileSize += int(match.group(2))
        if lastStopped == 10:
            lastStopped = 0
            showMatrix(totalFileSize, statusCodeCount)
    showMatrix(totalFileSize, statusCodeCount)


if __name__ == "__main__":
    run()
