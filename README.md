# devops_django_project_instagram

---

## 프로젝트 소개

해당 프로젝트는 SUS8기 개발 수업에서 진행한 Instagram 클론 코딩 프로젝트입니다. 해당 프로젝트는 Django 웹 프레임워크를 사용하여 개발되었습니다.

## 실행 방법

```
# 1. 먼저 Python 가상 환경을 생성 (Miniconda 등의 가상 환경 도구 필요)
conda create -n 가상환경이름 python=3.10 이상

# 2. 생성한 가상 환경을 활성화
conda activate 가상환경의 이름

# 3. 프로젝트에 필요한 패키지를 설치
pip install -r requirements.txt

# 4. Django 데이터베이스를 migrate 명령어로 DB 생성
python manage.py makemigrations
python manage.py migrate

# Django 개발 서버를 실행
python manage.py runserver

# 웹 브라우저에서 `http://127.0.0.1:8000/main/` 주소로 접속하여 프로젝트를 확인
http://127.0.0.1:8000/main/
```

## 필요한 환경

- Python 3.10 이상
- Django 3.x 이상
- `requirements.txt` 파일에 명시된 Python 패키지
