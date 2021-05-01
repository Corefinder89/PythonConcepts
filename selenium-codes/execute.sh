#!/bin/bash

# Check if html_reports directory is present
if [ -d "html_reports" ]; then
    echo "html_reports already present in path"
else
    mkdir html_reports
    echo "directory html_reports created"
fi

pytest test -s -v --html=html_reports/reports.html --log-file logs/"$(date '+%F_%H:%M:%S')".log