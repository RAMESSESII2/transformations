from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 0 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Linux, Windows',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='transform',
  version='0.1',
  description='A Computer Graphics library to implement and visulaize how founding algorithms of Graphics work.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Satyam Bhardwaj',
  author_email='stmbhardwaj@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='transform, 2d, computer-graphics', 
  packages=find_packages(),
  install_requires=[''] 
)