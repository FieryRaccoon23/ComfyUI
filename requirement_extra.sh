#!/usr/bin/env bash
set -e

python3 -m pip install -U crawl4ai
crawl4ai-setup
crawl4ai-doctor
echo "Done."