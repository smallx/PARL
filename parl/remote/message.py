#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os


class AllocatedGpu(object):
    def __init__(self, worker_address, gpu):
        """
        Args:
            gpu(str): a comma separated list of GPU(s) used in a job
        """
        self.worker_address = worker_address
        self.gpu = gpu


class AllocatedCpu(object):
    def __init__(self, worker_address, n_cpu):
        """
        Args:
            n_cpu(int): The number of CPU(s) used in a job.
        """
        self.worker_address = worker_address
        self.n_cpu = n_cpu


class InitializedJob(object):
    def __init__(self,
                 job_address,
                 worker_heartbeat_address,
                 ping_heartbeat_address,
                 worker_address,
                 pid,
                 job_id=None,
                 log_server_address=None):
        """
    Args:
      job_address(str): Job address to which the new task connect.
      worker_heartbeat_address(str): Optional. The address to which the worker sends heartbeat signals.
      ping_heartbeat_address(str): the server address to which the client sends ping signals.
                                    The signal is used to check if the job is alive.
      worker_address(str): Worker's server address that receive command from the master.
      pid(int): Optional. Process id of the job.
      is_alive(True): Optional. This flag is used in worker to make sure that only alive jobs can be added into the worker_status.
    """
        self.job_address = job_address
        self.worker_heartbeat_address = worker_heartbeat_address
        self.ping_heartbeat_address = ping_heartbeat_address
        self.worker_address = worker_address
        self.pid = pid
        self.is_alive = True
        self.job_id = job_id
        self.log_server_address = log_server_address
        self.allocated_cpu = None  # Record CPU(s) used in a job
        self.allocated_gpu = None  # Record GPU(s) used in a job


class InitializedWorker(object):
    def __init__(self, worker_address, initialized_jobs, allocated_cpu, allocated_gpu, hostname):
        """
    Args:
        worker_address (str): Worker server address that receives commands from the master.
        initialized_jobs (list): A list of ``InitializedJob`` containing the information for initialized jobs.
        allocated_cpu (``AllocateCpu``): The allocation information of CPU
        allocated_gpu (``AllocateGpu``): The allocation information of GPU
    """
        self.worker_address = worker_address
        self.initialized_jobs = initialized_jobs
        self.allocated_cpu = allocated_cpu
        self.allocated_gpu = allocated_gpu
        self.hostname = hostname
