#!/usr/bin/env bash
# Generate security documentation for the GSA PSHC discovery application.

SCRIPT_DIR="$(cd "$(dirname "$([ `readlink "$0"` ] && echo "`readlink "$0"`" || echo "$0")")"; pwd -P)"
cd "$SCRIPT_DIR/.."

echo "Fetching compliance definition dependencies into opencontrols directory"
compliance-masonry get

echo "Generating security documentation"
compliance-masonry docs gitbook --markdowns compliance/markdown --exports opencontrols/export LATO
