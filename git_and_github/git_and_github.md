# Git과 Github 공부
## 최초 설정
```
git.config --global user.name "이름" 

git.config --global user.email "메일주소"
```
## 저장소 사용하기
* 저장소 생성& 초기화
```
git init
```
* 원격저장소 내용 복제
```
git clone
```
## 브랜치 관리
### 브랜치 확인
```
git branch
```
### 브랜치 생성
```
git branch <브랜치>
ex) git branch test
```
### 브랜치 전환하기
```
git checkout <사용할 브랜치>
ex) git checkout test
```
### 브랜치 생성과 동시에 전환
```
git checkout -b <브랜치>
```
### 브랜치 병합하기
현재 브랜치에 <병합할 브랜치>를 병합함 → 현재 브랜치를 잘 확인하기
```
git merge <병합할 브랜치 이름>
```
### 브랜치 삭제
```
git branch -d <삭제할 브랜치>
```