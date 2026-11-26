$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not available in PATH. Install Git first."
}

if (-not (git config user.name)) {
    throw "Git user.name is not set. Run: git config --global user.name `"Your Name`""
}
if (-not (git config user.email)) {
    throw "Git user.email is not set. Run: git config --global user.email `"you@example.com`""
}

if (-not (Test-Path ".git")) {
    git init
    git branch -M main
    git add -A
    git commit -m "chore: initialize project scaffold"
} else {
    Write-Host "Git repository already initialized; skipping initial commit."
}

$branches = @(
    "feature/data-preprocessing",
    "feature/lstm-model",
    "feature/gru-model",
    "feature/baseline-evaluation",
    "feature/integration-demo"
)

foreach ($branch in $branches) {
    $existing = git branch --list $branch
    if ($existing) {
        Write-Host "Branch already exists: $branch"
    } else {
        git branch $branch main
        Write-Host "Created branch: $branch"
    }
}

Write-Host "`nBranches ready. Current branch remains unchanged."
git branch --list
