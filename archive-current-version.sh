#!/bin/bash

# Archive Current Version Script
# This script creates a permanent archive of the current version before implementing v2.0 changes

echo "  VaquarKhan Protocol Version Archiving Script"
echo "================================================"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo " Error: Not in a git repository. Please run this from the repository root."
    exit 1
fi

# Get current date for tagging
CURRENT_DATE=$(date +"%Y-%m-%d")

echo " Current repository status:"
git status --short

echo ""
read -p " Do you want to commit any pending changes before archiving? (y/n): " commit_changes

if [ "$commit_changes" = "y" ] || [ "$commit_changes" = "Y" ]; then
    echo " Committing current changes..."
    git add .
    git commit -m "Final commit before VaquarKhan Protocol v2.0 mathematical corrections - $CURRENT_DATE"
fi

echo ""
echo "  Creating archive tag for v1.0 (Original Khan Index)..."
git tag -a "v1.0-original-khan-index" -m "Original Khan Index formulation before mathematical corrections (archived $CURRENT_DATE)"

echo " Pushing archive tag to remote..."
git push origin v1.0-original-khan-index

echo ""
echo " Creating archive branch..."
git checkout -b "archive/v1.0-original-formulation"
git push origin "archive/v1.0-original-formulation"

echo " Returning to main branch..."
git checkout main

echo ""
echo " Archive Complete!"
echo " Archive locations:"
echo "   • Git Tag: v1.0-original-khan-index"
echo "   • Branch: archive/v1.0-original-formulation"
echo "   • Documentation: VERSION-HISTORY-DETAILED.md"
