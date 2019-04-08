import asyncio
from os import write as file_write

class FileReader():
    def __init__():
        self.block_queue = asyncio.Queue() 
        pass

    def start(self):
        while True:
            block = await self.block_queue.get()

            if !block:
                pass # Add some loggin

            block_abs_path, block_data = block
            file_write(block_abs_path, block_data)
