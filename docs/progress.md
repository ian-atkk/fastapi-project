FastAPI Project Reproduction

- Created a simple FastAPI service using uv for dependency management.
- Used pyproject.toml and uv.lock to manage and lock project dependencies.
- Cloned the project into a clean Ubuntu Docker environment.
- Successfully reproduced the toolchain with mise and project dependencies with uv.
- Confirmed the FastAPI endpoint runs successfully in the reproduced environment.

Github Runner and automate mise, ty, ruff check
- installed ty and ruff
- wrote project-runner.yml as github actions
    - confirmed that runs result in failure when bad code(code that doesn't pass ruff/ty) is pushed

Add Shellcheck(Shell Script) and cocogitto (commit history checks)
- install shellcheck: mise use shellcheck@0.11.0
    - use: mise exec -- shellcheck script.sh 
- install cocogitto: mise use cocogitto@7.0.0
    - use: mise exec -- cog check  
- confirmed it works locally
- added to github actions and confirm workflow fails with bad commit msg, or bad shell script

Add Syft(SBOM generator) and Grype (The Vulnerability Scanner)
- install syft: mise use syft@1.57.1
    - convert project dir to SBOM and save to JSON:mise exec -- syft . -o cyclonedx-json=sbom.cdx.json
- install grype: mise use grype@0.121.3
    - run a vulnerability db scan: mise exec -- grype sbom:./sbom.cdx.json

Comments: For the sbom/vulnerability check, the SBOM will be created before release, and will potentially be uploaded to github and pulled every week and checked with the database. Ig this is supposed to be automated? The other format/lint checks should be done when a pr is made or main is pushed. 

- added release-sbom runner to install mise, generate sbom, then run a vulnerability scan and save the results.json as an artifact.