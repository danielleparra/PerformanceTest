from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task
    def get_tests(self):
        self.client.get("")

    @task
    def put_tests(self):
       self.client.post("/p/login?txtUrl=%2F", {
        "name": "Labifas",
        "description": "senha"
         })


class WebsiteUser(HttpLocust):
    task_set = UserBehavior