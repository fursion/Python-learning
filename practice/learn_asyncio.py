# asyncio
import asyncio
import time


class Response:
    status_cede = 200


async def sim_request(index):
    print(f"模拟发送请求 Index: {index}")
    response = Response()
    await asyncio.sleep(1)
    print(f"request index : {index}, response status_code: {response.status_cede}")
    return  response.status_cede


task_loop = asyncio.get_event_loop()

task_array = []
for i in range(1000):
    task_array.append(sim_request(i))

# task_loop.run_until_complete(asyncio.wait(task_array))
result = task_loop.run_until_complete(asyncio.gather(*task_array))
print(result)
task_loop.close()