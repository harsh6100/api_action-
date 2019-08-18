import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
	res = requests.get(url)
	status=res.status_code
        print(status)

        if status == 200:
            return (True, status)
        return (False, status)
