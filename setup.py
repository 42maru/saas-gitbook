from setuptools import setup, find_packages

version = dict()
with open('./f2maru_qa/version.py') as fp:
    exec(fp.read(), version)

setup(
    name='f2maru_qa',
    version=version['__version__'],
    description='42Maru QA Engine Client',
    author='dante',
    author_email='dante@42maru.com',
    url='https://github.com/42maru/42maru-qa-client-python',
    download_url='https://github.com/42maru/42maru-qa-client-python/archive/master.zip',
    packages=find_packages(exclude=['tests', 'sample']),
    keywords=['QA engine', 'search', 'MRC', 'machine reading comprehension'],
    python_requires='>=3.6',
    license='MIT',
    install_requires=[
        'requests[security]>=2.9.1',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
)
