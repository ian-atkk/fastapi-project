FastAPI Project Reproduction

- Created a simple FastAPI service using uv for dependency management.
- Used pyproject.toml and uv.lock to manage and lock project dependencies.
- Cloned the project into a clean Ubuntu Docker environment.
- Successfully reproduced the toolchain with mise and project dependencies with uv.
- Confirmed the FastAPI endpoint runs successfully in the reproduced environment.

Github Runner and automate mise, ty, ruff check
- installed ty and ruff
- wrote project-runner.yml as github actions
    - confirmed that failure happened when bad code is pushed