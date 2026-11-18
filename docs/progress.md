**FastAPI Project Reproduction**

- Created a simple FastAPI service using uv for dependency management.
- Used pyproject.toml and uv.lock to manage and lock project dependencies.
- Cloned the project into a clean Ubuntu Docker environment.
- Successfully reproduced the toolchain with mise and project dependencies with uv.
- Confirmed the FastAPI endpoint runs successfully in the reproduced environment.

**Github Runner and automate mise, ty, ruff check**
- installed ty and ruff
- wrote project-runner.yml as github actions
    - confirmed that runs result in failure when bad code(code that doesn't pass ruff/ty) is pushed

**Add Shellcheck(Shell Script) and cocogitto (commit history checks)**
- install shellcheck: mise use shellcheck@0.11.0
    - use: mise exec -- shellcheck script.sh 
- install cocogitto: mise use cocogitto@7.0.0
    - use: mise exec -- cog check  
- confirmed it works locally
- added to github actions and confirm workflow fails with bad commit msg, or bad shell script

**Add Syft(SBOM generator) and Grype (The Vulnerability Scanner)**
- install syft: mise use syft@1.57.1
    - convert project dir to SBOM and save to JSON:mise exec -- syft . -o cyclonedx-json=sbom.cdx.json
- install grype: mise use grype@0.121.3
    - run a vulnerability db scan: mise exec -- grype sbom:./sbom.cdx.json

Comments: For the sbom/vulnerability check, the SBOM will be created before release, and will potentially be uploaded to github and pulled every week and checked with the database. Ig this is supposed to be automated? The other format/lint checks should be done when a pr is made or main is pushed. 

- added release-sbom runner to install mise, generate sbom, then run a vulnerability scan and save the results as an artifact.
-Results of vulnerable software results: 

SyntaxError: JSON.parse: unexpected character at line 1 column 1 of the JSON data

NAME      INSTALLED  FIXED IN  TYPE    VULNERABILITY        SEVERITY  EPSS         RISK   
requests  2.30.0     2.31.0    python  GHSA-j8r2-6x86-q33q  Medium    3.0% (87th)  1.7    
requests  2.30.0     2.32.4    python  GHSA-9hjg-9r4m-mvj7  Medium    1.0% (64th)  0.5    
requests  2.30.0     2.32.0    python  GHSA-9wx4-h78v-vm56  Medium    0.3% (27th)  0.2    
requests  2.30.0     2.33.0    python  GHSA-gc5v-m9x4-r6x2  Medium    0.2% (9th)   < 0.1

Instructions for required actions:
- ci.yml (Pull Requestを受け付けたときに実行)
投げられたパッチが正しいかチェックをします。基本的にはコードのlintチェック、コードのビルドチェック、テストを実施ます。
ドキュメントの更新のみのパッチ、テストスクリプトの変更だけのパッチでコードのビルド等が動かないようにpath-filterを設定すると良いです。
- release.yml (ソフトウェアのリリース作業、手動で実行、もしくは正式バージョンのタグを持つコミットが行われたとき実行)
- releaseモードでコードをビルド、所定の場所へのアップロードをします。
今回から、それに加えSBOMの生成も行います。
^ security_audit.yml (脆弱性チェック、最低１日１回実行)
過去に生成されたSBOMを使って脆弱性のチェックを行う
- check_package_vulns.yml (開発ツール,外部packageの脆弱性チェック、1周間に１回)