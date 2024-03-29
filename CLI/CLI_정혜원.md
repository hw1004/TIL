**GUI (Graphic User Interface)**
- *Interface* : 서로 다른 두 존재 간의 접점
- *UI(User Interface)의 개선은 UX(User experience)의 향상임*
- 물리적 Interface의 예시 : HDMI (모니터와 컴퓨터 연결)

**CLI (Command Line Interface)**

|명령어|설명|예시|
|---|---|---|
|$|터미널에 명령어 입력 준비| |
|pwd|print working directory(현재 디렉토리 경로 알려줌)||
|mkdir|폴더를 생성한다|`$ mkdir my_dir`|
|touch|파일을 생성한다|`$ touch a.txt`|
|rm|파일을 삭제한다|`$ rm a.txt`|
|rm -r|폴더를 삭제한다|`$ rm -r my_dir`|
|mv a b|파일/폴더명 a에서 b로 변경 OR 파일/폴더 a를 경로 b로 이동|`$ mv git github`, `$ mv github TIL`, `$ mv a ..`: a 파일을 지금 폴더의 전 폴더로 이동|
|cp a b|파일 a를 b로 복사|`$ cp a.txt copy/`|
|cp -r a b|폴더 a를 b로 복사|`$ cp -r python CLI`|
|ls|현재 위치 폴더 또는 특정 경로의 모든 하위 항목 표시|`$ ls`, `$ ls python`|
|cat|파일 내용 출력|`$ cat gui_and_cli.md`|
|cd|폴더 이동|`$ cd my_dir`|
|ctrl + l|터미널 정리(clear)| |
|ctrl + c|취소(cancle)| |
|~|홈(Home) 폴더 상징 기호|`$ cd ~`|
|/|최상단(Root) 폴더 상징 기호|`$ cd /`|
|.|현재 위치 상징 기호|`$ code .`|
|..|현재 기준 상위 폴더 상징 기호|`$ cd ..`|