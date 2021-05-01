#!/bin/bash

# Check if html_reports directory is present
if [ -d "html_reports" ]; then
    echo "directory html_reports already present in path"
else
    mkdir html_reports
    echo "directory html_reports created"
fi

# Check if html_reports directory is present
if [ -d "logs" ]; then
    echo "directory logs already present in path"
else
    mkdir logs
    echo "directory logs created"
fi

pytest test -s -v -m execute --html=html_reports/reports.html --log-file logs/"$(date '+%F_%H:%M:%S')".log