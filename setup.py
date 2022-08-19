# setup.py 파일이 있으면 pip로 설치가 가능하다.
from gettext import install
from setuptools import setup

setup(
    name="myapi", #자신의 라이브러리 이름. 먄약 언더바 _ 를 붙이면 자동으로 하이픈 - 으로 바뀌어 저장된다.
    version= "0.0.1",  #릴리즈넘버(큰 변화가 일어났을 시).메이저넘버(기능추가, 기능수정이 많이 일어났을 때).마이너넘버(버그나 보안 수정)
    description= "my api lib", #설명
    url= "https://github.com/WhiteChaplin/api_project.git",
    author= "WhiteChaplin",
    author_email= "nsn1180@gmail.com",
    packages= ["my_api"], #소스가 저장되어 있는 폴더
    install_requires = [ #사용시 필요한 라이브러리 이름. yaml은 올리지 않기에 추가하지 않음 
        "requests"
    ]
)