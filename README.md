# 브랜치 정책 설정

## GitHub 브랜치 보호 설정

### 📍 설정 경로
Repository → Settings → Branches → Add classic branch protection rule

### ✅ 설정 항목
- **Branch name pattern**: `main`
- **Require a pull request before merging**
  - `Require approvals`: 최소 승인 인원 수 지정
- **Require status checks to pass before merging**
  - merge 하기 전에 반드시 status check을 통과해야 함
  - 필요 이유: 코드 구현을 간단하게 하더라도 가끔 빌드가 되지 않는 경우가 발생함.
  - 코드 작성에 집중하고 빌드 여부는 GitHub Action이 자동으로 확인 후 status check을 제공
- **Require branches to be up to date before merging**
  - 모든 브랜치는 병합 전에 최신 상태를 유지해야 함
- **Do not allow bypassing the above settings**
  - 위 설정을 우회하는 것을 허용하지 않음

### 🔹 브랜치 보호 정책
- `main` 브랜치에 직접 수정을 가할 수 없음
- 새로운 브랜치를 생성하여 작업 후, `main` 브랜치에 병합 시 반드시 **PR(Pull Request)**을 요청해야 함
- PR을 요청하더라도 **즉시 merge되지 않고, 최소 인원 수 이상의 리뷰를 받아야 merge 가능**
- 사람이 많아질수록 `main` 브랜치를 보호하기 어려워지므로, 브랜치 분리를 통해 관리
- **Merge 하기 전에 반드시 충족해야 하는 두 가지 조건**
  1. Status check이 성공해야 함
  2. 최소 한 명 이상의 PR 승인이 필요

