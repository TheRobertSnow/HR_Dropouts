import sys
sys.path.append('..')
import IOAPI

class WorkerLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()
        self.get_worker_list()

    def get_worker_list(self):
        self.worker = self.IOAPI.request_workers()

    def find_worker_by_ID(self, id):
        for instance in self.worker:
            if instance.workerID == id:
                print(instance)

# +++++++++ Test Case ++++++++++
# workerLL = WorkerLL()
# workerLL.find_worker_by_ID("1")
