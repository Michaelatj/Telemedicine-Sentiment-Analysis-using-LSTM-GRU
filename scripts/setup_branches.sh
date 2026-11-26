#!/usr/bin/env bash
set -euo pipefail

command -v git >/dev/null 2>&1 || { echo "Git is not installed." >&2; exit 1; }

git config user.name >/dev/null || { echo 'Set git config --global user.name "Your Name" first.' >&2; exit 1; }
git config user.email >/dev/null || { echo 'Set git config --global user.email "you@example.com" first.' >&2; exit 1; }

if [ ! -d .git ]; then
  git init
  git branch -M main
  git add -A
  git commit -m "chore: initialize project scaffold"
else
  echo "Git repository already initialized; skipping initial commit."
fi

branches=(
  "feature/data-preprocessing"
  "feature/lstm-model"
  "feature/gru-model"
  "feature/baseline-evaluation"
  "feature/integration-demo"
)

for branch in "${branches[@]}"; do
  if git show-ref --verify --quiet "refs/heads/$branch"; then
    echo "Branch already exists: $branch"
  else
    git branch "$branch" main
    echo "Created branch: $branch"
  fi
done

echo
echo "Branches ready. Current branch remains unchanged."
git branch --list
