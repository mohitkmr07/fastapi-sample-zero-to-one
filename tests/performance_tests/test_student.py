from locust import HttpUser, task, between


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_get_students_by_id(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.get("/v1/students/62c5454e725245bef65ecf20", headers=headers)
