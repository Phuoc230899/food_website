import asyncio

async def sum(name,arr):
    for number in arr :
        print(name+" "+str(number))
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A",[1,2,3])),
    loop.create_task(sum("B",[4,5,6]))
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print('Xin chào bản test git')
