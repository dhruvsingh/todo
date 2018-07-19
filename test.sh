
curl \
--header "Content-type: application/json" \
--request POST \
--data '{"state": "1", "text": "Task 1", "due_date":"2018-09-20T22:59:00"}' \
http://localhost:8000/api/task/


curl \
--header "Content-type: application/json" \
--request GET \
http://localhost:8000/api/task/


curl \
--header "Content-type: application/json" \
--request PUT \
--data '{"state": "2", "text": "Task 1", "due_date":"2018-09-20T22:59:00"}' \
http://localhost:8000/api/task/1/

curl \
--header "Content-type: application/json" \
--request GET \
http://localhost:8000/api/task/

curl \
--header "Content-type: application/json" \
--request POST \
--data '{"state": "1", "text": "Task 2", "due_date":"2018-09-20T22:59:00"}' \
http://localhost:8000/api/task/

curl \
--header "Content-type: application/json" \
--request GET \
http://localhost:8000/api/task/


curl \
--header "Content-type: application/json" \
--request DELETE \
http://localhost:8000/api/task/1/


curl \
--header "Content-type: application/json" \
--request GET \
http://localhost:8000/api/task/
