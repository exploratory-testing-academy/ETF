# README
Tests in this repository run on Docker with Python 3.9.*

Includes:  
  * tests using browser (playwright) library
  * tests using pabot to parallelize test runs when needed
  * failing tests on webkit -- comparison seems to be broken 

## Running tests Locally

Getting started:
  * install requirements ```pip install -r requirements.txt```
  * install dependencies ```rfbrowser init```
  
To run tests from command line, use

```robot <i>filename</i>```
```robot -i <i>tag</i> <i>filename</i>```

Update browser library locally, it gets updated automatically within the docker
```pip install --upgrade robotframework-browser```
```rfbrowser init```

## Running tests in Docker
Get the baseline docker image:
```docker pull mcr.microsoft.com/playwright:focal```

Build docker: 
```docker build --tag eprime-tests .```

Run on mac/linux:
```docker run --rm --net=host --security-opt seccomp:unconfined --shm-size "256M" -v $PWD:/app eprime-tests```

Run on win:
```docker run --rm --net=host --security-opt seccomp:unconfined --shm-size "256M" -v <YOUR PROJECT LOCATION>:/app eprime-tests```

```docker run --rm --net=host --security-opt seccomp:unconfined --shm-size "256M" -v C:\BitbucketRepos\ETF\tests-in-docker:/app eprime-tests```

Cleanup:
```docker system prune -a --force```

## Running Pabot tests
Pabot tests allow parallel execution of Robot tests. To run Pabot tests, update ```Dockerfile``` and
enable *perf_test_env* script while disabling *test_env* script and build:

```
ENTRYPOINT ["/app/scripts/entrypoint_perf_test.sh"]
#ENTRYPOINT ["/app/scripts/entrypoint_test.sh"]
```

Additionally, edit ```./scripts/Dockerfile/entrypoint_perf_test_env.sh``` file to add more Pabot tests.

## References
* https://pypi.org/project/robotframework-browser/
