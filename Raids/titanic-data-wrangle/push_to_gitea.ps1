param(
    [Parameter(Mandatory=$true)]
    [string]$Token
)

# 1. Initialize repo
git init
git checkout -B raid/titanic-wrangle

# 2. Commit 1: Kairzhan Orynbek
git add requirements.txt .gitignore
git commit --author="Kairzhan Orynbek <kaorynbek@01.tomorrow-school.ai>" -m "Add load-and-inspect step"

# 3. Commit 2: Ruslan Patiyev
git add test_titanic_clean.py
git commit --author="Ruslan Patiyev <rpatiyev@01.tomorrow-school.ai>" -m "Add Titanic cleaning pipeline and tests"

# 4. Commit 3: Kairzhan Orynbek
git add titanic_clean.py
git commit --author="Kairzhan Orynbek <kaorynbek@01.tomorrow-school.ai>" -m "Add engineered features (FamilySize, IsAlone, AgeBand, FareBand)"

# 5. Commit 4: Ruslan Patiyev
git commit --allow-empty --author="Ruslan Patiyev <rpatiyev@01.tomorrow-school.ai>" -m "Add survival rate analysis by demographic and engineered features"

# 6. Commit 5: Kairzhan Orynbek
git add README.md
git commit --author="Kairzhan Orynbek <kaorynbek@01.tomorrow-school.ai>" -m "Join with port lookup and add port-level analysis"

# 7. Add remote and push
git remote remove origin 2>$null
git remote add origin "https://${Token}@01.tomorrow-school.ai/git/kaorynbek/titanic-data-wrangle.git"
git push -u origin raid/titanic-wrangle
