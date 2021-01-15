# README
Tests in this repository require any Python version that is between 3.8.5 - 3.8.9 but must not be Python 3.9.*

## Running tests in Docker

Includes:  
  * tests using browser (playwright) library
  * tests using pabot to parallelize test runs when needed

Getting started:
  * install requirements ```pip install -r requirements.txt```
  * install dependencies ```rfbrowser init```
  
To run tests from command line, use

```robot <i>filename</i>```
```robot -i <i>tag</i> <i>filename</i>```

Update browser library locally, it gets updated within the docker
```pip install --upgrade robotframework-browser```
```rfbrowser init```

Build docker:
```docker build --tag eprime-tests .```
On mac/linux:
```docker run --rm --net=host --security-opt seccomp:unconfined --shm-size "256M" -v $PWD:/app eprime-tests```
On win:
```docker run --rm --net=host --security-opt seccomp:unconfined --shm-size "256M" -v <YOUR PROJECT LOCATION>:/app eprime-tests```
Cleanup:ß
```docker system prune -a --force```

## Running Pabot tests
Pabot tests allow parallel execution of Robot tests. To run Pabot tests, update ```Dockerfile``` and
enable *perf_test_env* script while disabling *test_env* script:
```
ENTRYPOINT ["/app/scripts/entrypoint_perf_test.sh"]
#ENTRYPOINT ["/app/scripts/entrypoint_test.sh"]
```
Additionally, edit ```./scripts/Dockerfile/entrypoint_perf_test_env.sh``` file to add more Pabot tests.


## References
* https://pypi.org/project/robotframework-browser/