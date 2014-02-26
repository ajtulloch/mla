python frontend/run.py &
FRONTEND_PID=$!

python worker/main.py localhost training_requests reports &
WORKER_PID=$!

python regression_testing/main.py http://localhost:5000/

sleep 50

kill -9 $FRONTEND_PID
kill -9 $WORKER_PID
