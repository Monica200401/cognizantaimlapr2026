import asyncio
import time
async def create_clock():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))
        """
        pauses the execution of the current task for 1 second, allowing other tasks to run during that time.
        """
        await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(create_clock())
   
 