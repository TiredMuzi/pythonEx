import os, glob, shutil

#작업 폴더 가져오기 
# print("======= 작업 폴더 가져오기")
# print(os.getcwd())

#작업 폴더 변경 
#os.chdir('d:\\myWork\\pyEx')
#os.chdir(r'd:\myWork\pyEx')

# 폴더 유무 확인과 생성 
# print("======= 폴더 유무 확인")
# print( os.path ) 
# print( os.path.exists('D:\\myWork\\github\\pythonEx\\ch3\\csv_card.py') )
# print( os.path.isdir('csv_card.py') )

# 폴더 생성
# if not os.path.exists('data'):
#     os.mkdir('data')
    
# 파일 가져오기
# print( glob.glob('*') ) 
# print( glob.glob('D:\\myWork\\github\\pythonEx\\ch3\\*.py') )
# DOC로 시작하는 파일 가져오기 
# print( glob.glob('D:\\myWork\\github\\pythonEx\\ch3\\doc*.py') )
# read로 끝나는 파일 가져오기 
# print( glob.glob('D:\\myWork\\github\\pythonEx\\ch3\\*read.py') )

# 상대 경로를 절대 경로로 변경
# 절대경로 : 윈도우 c:\test\test\   맥 : /test/test/
# print( os.getcwd() ) 
# print( os.path.abspath('../'))
# print( os.path.abspath('.'))

# 절대 경로에서 폴더 경로 또는 파일명만 가져오기 
# testDir = 'D:\\myWork\\github\\pythonEx\\ch3\\csv_card.py'
# print( os.path.dirname( testDir ) )         # 폴더 경로
# print( os.path.basename( testDir ) )        # 파일명 

# os 의존 없이 경로 결합하기 
# print( os.path.join('myWork','github','pythonEx') )

# 프로그램 자신을 나타내는 __file__
# path1 = os.path.abspath('./ch3/input/name1.xlsx')
# print(path1)

# 실행중인 프로그램 경로 기준으로 파일의 절대 경로 얻기 
# base_dir = os.path.dirname(__file__)
# path2 = os.path.join(base_dir, 'input','name1.xlsx')
# path2 = os.path.abspath(path2)
# print(path2)

# 그 외 명령어들 
# os.chdir(path)                          # 작업 디렉터리를 path로 변경   
# os.chmod(path, mode)                    # path의 파일 속성을 mode로 변경
# os.mkdir(path, mode=0o777)              # path에 폴더를 만들고 mode로 파일 속성 설정 
# os.remove(path)                         # path 파일 삭제
# os.rmdir(path)                          # path 폴더 삭제(단, 폴더가 비어 있어야 함)
# os.rename(src, dist)                    # 파일명을 src에서 dist로 변경 
# os.stat(path)                           # 파일(폴더)path의 정보 가져오기 
# os.symlink(src, dist)                   # src를 가리키는 심볼릭 링크를 dist로 작성 

# print( os.name        )                         # os의 모듈명 반환 (윈도우는 nt 맥/리눅스는 posix)
# print( os.getenv('JAVA_HOME') )                 # 환경변수 key의 값을 반환 
# print( os.getlogin()  )                         # 로그인한 유저명을 반환 
# print( os.cpu_count() )                         # 시스템의 cpu수를 반환
# print( os.sep         )                         # 경로를 구분하는 기호  
                        
# 파일 복사 
# shutil.copytree('D:\\myWork\\github\\pythonEx\\ch3', 'D:\\myWork\\github\\pythonEx\\ch3333')

# 폴더 삭제 
shutil.rmtree('D:\\myWork\\github\\pythonEx\\ch3333')