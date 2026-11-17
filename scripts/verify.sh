#!/usr/bin/env bash
set -euo pipefail

name="${1:-world}"

echo "Hello, ${name}!"
echo "Today is $(date +%Y-%m-%d)"
echo "Current directory: $(pwd)"

if [[ -d "$HOME" ]]; then
  echo "Home directory exists: $HOME"
fi

exit 0
