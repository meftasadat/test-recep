#!/usr/bin/env bash
docker build -t test-recep .
docker run -v $(pwd)/:/work_dir -it --rm test-recep bash